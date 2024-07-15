from typing import Any
from django.views.generic import TemplateView
import requests
from .like import getLikesByType


class SportsView(TemplateView):
    template_name = "sports.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['teams'] = getTeams(self)
        return context


def getTeams(self):
    url = "https://v3.football.api-sports.io/teams?league=61&season=2024"

    payload = {}
    headers = {
        'x-apisports-key': 'a71309624efcc0969da5ce7b53a68dce'
    }

    res = requests.request("GET", url, headers=headers, data=payload)

    likes = getLikesByType(request=self.request, tag="team")
    teams = []
    for teamObj in res.json()['response']:
        el = {
            'id': teamObj['team']['id'],
            'name': teamObj['team']['name'],
            'logo': teamObj['team']['logo'],
            'stade': teamObj['venue']['name'],
            'isLiked': str(teamObj['team']['id']) in likes
        }
        teams.append(el)
    return teams


def getLeagues():
    url = "https://v3.football.api-sports.io/leagues?country=World"

    payload = {}
    headers = {
        'x-apisports-key': 'a71309624efcc0969da5ce7b53a68dce'
    }

    res = requests.request("GET", url, headers=headers, data=payload)

    leagues = []
    for leagueObj in res.json()['response']:
        el = {
            'id': leagueObj['league']['id'],
            'name': leagueObj['league']['name'],
            'logo': leagueObj['league']['logo'],
            'country': leagueObj['country']['name'],
        }
        leagues.append(el)
    print(leagues)
    return leagues
