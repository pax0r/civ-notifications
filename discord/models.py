from django.db import models

from web.models import Game, Player


class DiscordWebhook(models.Model):
    name = models.CharField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    webhook_id = models.CharField(max_length=255)
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DiscordPlayerMapping(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name="discord")
    discord_id = models.CharField(max_length=255)

    def __str__(self):
        return '{} {}'.format(self.player.name, self.discord_id)
