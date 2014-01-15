from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Coach(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    start_year = models.IntegerField(max_length=4, blank=True)
    team = models.ManyToManyField(Team)

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

