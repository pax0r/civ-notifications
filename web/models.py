from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=255)


class LastPlayerTurnManager(models.Manager):
    def set_current_turn(self, game_name, civilization_nick, turn_number):
        game, created = Game.objects.get_or_create(
            name=game_name, defaults={'name': game_name}
        )

        obj, created = self.update_or_create(
            game=game,
            defaults={'civilization_nick': civilization_nick, 'game': game, 'turn_number': turn_number},
        )


class LastPlayerTurn(models.Model):
    last_changed = models.DateTimeField(auto_now=True)
    civilization_nick = models.CharField(max_length=255)
    turn_number = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    objects = LastPlayerTurnManager()