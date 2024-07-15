from typing import Any
from django.views.generic import TemplateView
import requests
from .like import getLikesByType


class MarvelView(TemplateView):
    template_name = "marvel.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['characters'] = getCharacter(self.request)
        return context


def getCharacter(request):
    res = requests.get(
        'https://gateway.marvel.com/v1/public/characters?ts=1&apikey=eb79c3a5b07c45555c5af6c1ca4be64e&hash=5d78ad0af67862c3371c9a88a590eba6').json()['data']['results']
    characters = []
    likes = getLikesByType(request=request, tag="marvel")
    for char in res:
        characters.append({
            'id': char['id'],
            'name': char['name'],
            'img': char['thumbnail']['path'] + '.' + char['thumbnail']['extension'],
            'isLiked': str(char['id']) in likes
        })

    return characters
