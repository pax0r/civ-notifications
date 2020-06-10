import requests
from django.core.exceptions import ObjectDoesNotExist
from django_rq import job

from discord.models import DiscordWebhook
from web.models import Game, Player


@job
def send_discord_webhook(discord_webhook_id, game_id, player_id, turn_number):
    webhook = DiscordWebhook.objects.get(pk=discord_webhook_id)
    game = Game.objects.get(pk=game_id)
    player = Player.objects.get(pk=player_id)
    try:
        nickname = player.discord.discord_id
    except ObjectDoesNotExist:
        nickname = player.name
    payload = {
        "content": "Gra: {}, Tura {}, Gracz: {}".format(game.name, turn_number, nickname),
        "allowed_mentions": {
            "parse": ["users"],
        }
    }
    requests.post(
        f"https://discord.com/api/webhooks/{webhook.webhook_id}/{webhook.token}",
        json=payload
    )
