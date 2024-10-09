from typing import Any
from django.views.generic import TemplateView
import requests
from .like import getLikesByType
from marvel import Marvel


class MarvelView(TemplateView):
    template_name = "marvel.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['characters'] = getCharacter(self.request)
        return context


def getCharacter(request):

    characters = []

    m = Marvel("eb79c3a5b07c45555c5af6c1ca4be64e",
               "19c715a294563ec5ede9d342f28a9af388d9b332")
    allChars = m.characters.all().get("data").get("results")
    print(allChars)

    # NORMAL WAY
    # res = requests.get(
    #     'https://gateway.marvel.com/v1/public/characters?ts=1&apikey=eb79c3a5b07c45555c5af6c1ca4be64e&hash=5d78ad0af67862c3371c9a88a590eba6', verify=False).json()['data']['results']
    likes = getLikesByType(request=request, tag="marvel")
    for char in allChars:
        characters.append({
            'id': char['id'],
            'name': char['name'],
            'img': char['thumbnail']['path'] + '.' + char['thumbnail']['extension'],
            'isLiked': str(char['id']) in likes
        })

    return characters
