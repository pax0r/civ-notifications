from django.contrib import admin

from discord.models import DiscordPlayerMapping, DiscordWebhook


@admin.register(DiscordWebhook)
class DiscordWebhookAdmin(admin.ModelAdmin):
    pass


@admin.register(DiscordPlayerMapping)
class DiscordPlayerMappingAdmin(admin.ModelAdmin):
    pass
