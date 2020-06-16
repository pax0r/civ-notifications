from django.db import models, transaction


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
        with transaction.atomic():
            game, created = Game.objects.get_or_create(
                name=game_name, defaults={'name': game_name}
            )
            player, created = Player.objects.get_or_create(
                name=civilization_nick, defaults={'name': civilization_nick}
            )
            try:
                obj = self.select_for_update().get(game=game)
                changed = False
                if obj.player != player or obj.turn_number != turn_number:
                    obj.player = player
                    obj.turn_number = turn_number
                    obj.save()
                    changed = True
            except LastPlayerTurn.DoesNotExist:
                obj = self.create(
                    player=player,
                    game=game,
                    turn_number=turn_number
                )
                changed = True
            return obj, changed


class LastPlayerTurn(models.Model):
    last_changed = models.DateTimeField(auto_now=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    turn_number = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    objects = LastPlayerTurnManager()
