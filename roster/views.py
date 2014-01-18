from django.shortcuts import render
from roster.models import Team, Coach, Player

def RosterView(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    coaches = Coach.objects.all()
    context = {'teams': teams, 'players': players, 'coaches': coaches}
    return render(request, 'roster/roster.html', context)

def CoachView(request):
    coaches = Coach.objects.all()
    context = {'coaches': coaches}
    return render(request, 'roster/coaches.html', context)