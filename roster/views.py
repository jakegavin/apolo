from django.shortcuts import render
from roster.models import Team, Coach, Player

def RosterView(request):
    gteam = Team.objects.get(name="Girls")
    bteam = Team.objects.get(name="Boys")
    boys = []
    girls = []
    for player in Player.objects.all():
        if player.team == gteam:
            girls.append(player)
        elif player.team == bteam:
            boys.append(player)
        else:
            pass
    coaches = Coach.objects.all()
    context = {'gteam': gteam, 'bteam': bteam, 'boys': boys, 'girls': girls, 'coaches': coaches}
    return render(request, 'roster/roster.html', context)

def CoachView(request):
    coaches = Coach.objects.all()
    context = {'coaches': coaches}
    return render(request, 'roster/coaches.html', context)
