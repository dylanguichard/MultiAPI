from typing import Any
from django.views.generic import TemplateView
import requests
from .like import getLikesByType


class AnimeView(TemplateView):
    template_name = "anime.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['animes'] = getAnimes(self.request)
        print(context['animes'])
        return context


def getAnimes(request):
    res = requests.get('https://api.jikan.moe/v4/anime')
    likes = getLikesByType(request=request, tag="anime")
    animes = []
    for anime in res.json()['data']:
        animes.append({
            'id': anime['mal_id'],
            'title': anime['title'],
            'img': anime['images']['jpg']['image_url'],
            'year': anime['year'],
            'genre': anime['genres'][0]['name'],
            'isLiked': str(anime['mal_id']) in likes
        })

    return animes
