from django.db import models

class File(models.Model):
    name = models.CharField(max_length=70, blank=False)
    author = models.CharField('Uploaded by', max_length=70, blank=True)
    resource = models.FileField(upload_to='resources/', blank=False)
    description = models.TextField(blank=True)
    last_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
        
    def image_url(self):
        return MEDIA_URL + self.image.name