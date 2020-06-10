import django.dispatch

turn_notifications = django.dispatch.Signal(providing_args=["game_id", "player_id", "turn_number"])
