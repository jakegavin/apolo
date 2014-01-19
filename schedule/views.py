from django.shortcuts import render, get_list_or_404
from schedule.models import Season, Tournament, Game

def ScheduleView(request):
    seasons = Season.objects.all()
    tournaments = sorted(Tournament.objects.all())
    games = sorted(Game.objects.all())   
    context = {'seasons': seasons, 'tournaments': tournaments, 'games': games}
    return render(request, 'schedule/schedule.html', context)
