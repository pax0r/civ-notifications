from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class LastPlayerTurnManager(models.Manager):
    def set_current_turn(self, game_name, civilization_nick, turn_number):
        game, created = Game.objects.get_or_create(
            name=game_name, defaults={'name': game_name}
        )
        player, created = Player.objects.get_or_create(
            name=civilization_nick, defaults={'name': civilization_nick}
        )
        obj, created = self.update_or_create(
            game=game,
            defaults={'player': player, 'game': game, 'turn_number': turn_number},
        )
        return obj


class LastPlayerTurn(models.Model):
    last_changed = models.DateTimeField(auto_now=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    turn_number = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    objects = LastPlayerTurnManager()
