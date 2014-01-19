from django.db import models
from datetime import datetime, timedelta
from roster.models import Team

def make_tuple(x):
    return (x, x)

class Season(models.Model):
    year_list = []        
    current_year = datetime.now().year
    for year in range(current_year-2, current_year+4):
        year_list.append(str(year))
    YEARS = map(make_tuple, year_list)
    
    year = models.CharField(choices=YEARS, default=str(current_year), max_length=4, unique=True)
    
    # Check this
    def __unicode__(self):
        return self.year + ' Season'

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    season = models.ForeignKey(Season)
    date_start = models.DateField(default=datetime.now().date)
    date_end = models.DateField(default=datetime.now().date)
    location = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name + ': ' + str(self.date_start)
    
    def get_info(self):
        return self.name + ': ' + str(self.date_start)

class Game(models.Model):
    tournament = models.ForeignKey(Tournament)
    location = models.CharField('Location (pool name)', max_length=120, blank=True)
    opponent = models.CharField(max_length=70)
    team = models.ForeignKey(Team)
    time = models.CharField(max_length=70, blank=True)
    date = models.DateField(blank=True)
    HA = ((True, 'Home'), (False, 'Away'))
    home = models.BooleanField('Home or Away', default=False, choices=HA)
    # TODO: Add validator so this matches '[WLT] \d+\s*-\s*\d+'
    result = models.CharField(max_length=20, blank=True)
    
    def comp(self):
        '''Determine whether Ashland is home or away and return the appropriate string
        to compare the teams in the matchup (either "vs" or "@")''' 
        if self.home:
            return "vs."
        else: 
            return "@"
    
    def __unicode__(self):
        g = self.comp()
        if self.result:
            return "Ashland " + str(self.team) + ' ' + g + ' ' + self.opponent + ' ' + str(self.date) + ' (' + self.result + ')'
        else: 
            return "Ashland " + str(self.team) + ' ' + g + ' ' + self.opponent + ' ' + str(self.date)
    
    def teams_matchup(self):
        g = self.comp()
        return "Ashland %s %s %s" % (str(self.team), g, self.opponent)