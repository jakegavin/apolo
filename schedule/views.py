from django.shortcuts import render, get_list_or_404
from schedule.models import Season, Tournament, Game

from datetime import datetime

def ScheduleView(request):
    seasons = Season.objects.all()
    
    def date_start(self):
        return self.date_start
    tournaments = sorted(Tournament.objects.all(), key=date_start)
    
    def game_info(self):
        return str(self.date) + self.time
    games = sorted(Game.objects.all(), key=game_info)


    def get_games(games, gtournament):
        '''Takes list of all games and a tournament.
        Returns a list of games in the tournament. '''
        game_list = []
        for game in games:
            if game.tournament == gtournament:
                game_list.append(game)
            else:
                pass
        return game_list

    # Create a schedule list. The first element is the tournament.
    # The second elemnt is a list of games in the tournament
    schedule = []
    for t in tournaments:
        tgames = get_games(games, t)
        app = [t, tgames]
        schedule.append(app)

    context = {'schedule': schedule}
    return render(request, 'schedule/schedule.html', context)
