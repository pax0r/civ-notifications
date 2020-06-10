from django.contrib import admin

from web.models import Player, Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
