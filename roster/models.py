from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Coach(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    photo = models.ImageField(upload_to='images/coaches/', null=True)
    # Photo url can be retrived with Coach.photo.url
    title = models.CharField(max_length=70, blank=True)
    email = models.CharField(max_length=200, blank=True)
    team = models.ManyToManyField(Team)
    bio = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name 


class Player(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    team = models.ForeignKey(Team)
    number = models.IntegerField(blank=True)
    position = models.CharField(max_length=35, blank=True)
    grad_year = models.IntegerField()
    active = models.BooleanField(default=True)
   
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
