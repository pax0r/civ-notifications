import json

from django.http import JsonResponse, HttpRequest
from django.views import View
from django.views.generic import TemplateView

from web.models import LastPlayerTurn


class CivWebhookHandler(View):
    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        game_name = data['value1']
        player_name = data['value2']
        turn_number = int(data['value3'])
        LastPlayerTurn.objects.set_current_turn(game_name, player_name, turn_number)
        return JsonResponse({'status': 'ok'})


class WhosTurnIsAnyway(TemplateView):
    template_name = 'whos_turn.html'

    def get_context_data(self, **kwargs):
        game_id = kwargs.get('game_id')
        turn = LastPlayerTurn.objects.get(game__pk=game_id)
        return {
            'game_name': turn.game.name,
            'player_name': turn.civilization_nick,
            'turn_number': turn.turn_number,
        }