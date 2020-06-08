import json

from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView

from web.models import LastPlayerTurn, Player, Game


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
        turn = get_object_or_404(LastPlayerTurn, game__pk=game_id)
        return {
            'game_name': turn.game.name,
            'player_name': turn.player.name,
            'turn_number': turn.turn_number,
        }

    def get(self, request: HttpRequest, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse(self.get_context_data(**kwargs))
        return super().get(request, *args, **kwargs)


class PlayerNotifier(TemplateView):
    template_name = 'turn_notificator.html'

    def get_context_data(self, **kwargs):
        game_id = kwargs.get('game_id')
        player_id = kwargs.get('player_id')
        turn = get_object_or_404(LastPlayerTurn, game__pk=game_id)
        player = get_object_or_404(Player, pk=player_id)
        return {
            'game_id': game_id,
            'game_name': turn.game.name,
            'player_name': player.name,
            'players_turn': player == turn.player,
        }

    def get(self, request: HttpRequest, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse(self.get_context_data())
        return super().get(request, *args, **kwargs)
