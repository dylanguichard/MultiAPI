from django.views.generic import TemplateView
import requests


class MusicView(TemplateView):
    template_name = "music.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)

        res = requests.get(
            'https://api.deezer.com/playlist/908622995?index=0&limit=10')
        print(res.json())

        musics = []
        for music in res.json()['tracks']['data']:
            musics.append({
                'id': music['id'],
                'title': music['title'],
            })
        context['musics'] = musics

        return context
