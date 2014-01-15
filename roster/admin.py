from django.contrib import admin
from roster.models import Team, Coach, Player

admin.site.register(Team)

class CoachAdmin(admin.ModelAdmin):
    pass

admin.site.register(Coach, CoachAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'number', 'grad_year')

admin.site.register(Player, PlayerAdmin)

