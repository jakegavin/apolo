from django.shortcuts import render
from roster.models import Team, Coach, Player

def index(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    coaches = Coach.objects.all()
    context = {'teams': teams, 'players': players, 'coaches': coaches}
    return render(request, 'roster/index.html', context)
