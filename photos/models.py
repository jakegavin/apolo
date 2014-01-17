import os
from os.path import join as pjoin, basename
from django.db import models
from django.core.files import File

from apolo.settings import MEDIA_ROOT, MEDIA_URL

from tempfile import NamedTemporaryFile
from PIL import Image as PImage


from common.utils import *


link = "<a href='%s'>%s</a>"

class Group(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    link=models.URLField(blank=True, null=True)
    hidden = models.BooleanField()
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self, show="thumbnails"):
        return reverse2("group", dpk=self.pk, show=show)
    
    def image_links(self):
        lst = [img.image.name for img in self.images.all()]
        lst = [link % ( MEDIA_URL+img, basename(img) ) for img in lst]
        return ", ".join(lst)
    image_links.allow_tags = True

imgtag = "<img border='0' alt='' src='%s' />"

class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/")
    thumbnail = models.ImageField(upload_to="images/", blank=True, null=True)
    
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    hidden = models.BooleanField()
    group = models.ForeignKey(Group, related_name="images", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.image.name
    
    class Meta:
        ordering = ['created']
    
    def get_absolute_url(self):
        return reverse2('image', mfpk=self.pk)
    
    def save(self, *args, **kwargs):
        """Save image dimensioins."""
        super(Image, self).save(*args, **kwargs)
        img = PImage.open(pjoin(MEDIA_ROOT, self.image.name))
        self.width, self.height = img.size
        self.save_thumbnail(img, (128,128))
        super(Image, self).save(*args, **kwargs)
        
    def save_thumbnail(self, img, size):
        fn, ext = os.path.splitext(self.image.name)
        img.thumbnail(size, PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb" + ext
        tf = NamedTemporaryFile()
        img.save(tf.name, "JPEG")
        thumbnail = getattr(self, "thumbnail")
        thumbnail.save(thumb_fn, File(open(tf.name)), save=False)
        tf.close()
    
    def size(self):
        return "%s x %s" % (self.width, self.height)
    
    def thumbnail_url(self):
        return MEDIA_URL + self.thumbnail.name
        
    def image_url(self):
        return MEDIA_URL + self.image.name
    