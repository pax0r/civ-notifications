from django.apps import AppConfig


def send_discord_notification(sender, game_id, player_id, turn_number, **kwargs):
    from discord.tasks import send_discord_webhook
    from discord.models import DiscordWebhook
    try:
        discord_webhook = DiscordWebhook.objects.get(game_id=game_id)
        send_discord_webhook.delay(
            discord_webhook_id=discord_webhook.pk,
            game_id=game_id,
            player_id=player_id,
            turn_number=turn_number,
        )
    except DiscordWebhook.DoesNotExist as e:
        pass


class DiscordConfig(AppConfig):
    name = 'discord'

    def ready(self):
        from web.signals import turn_notifications
        turn_notifications.connect(send_discord_notification)
