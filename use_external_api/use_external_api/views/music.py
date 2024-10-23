from django.views.generic import TemplateView
import requests


class MusicView(TemplateView):
    template_name = "music.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)

        chart_url = "https://api.deezer.com/chart/0/tracks"
        playlist_url = "https://api.deezer.com/playlist/908622995?index=0&limit=10"

        context['tracks'] = getChartTracks()

        return context


def getChartTracks():
    chart_url = "https://api.deezer.com/chart/0/tracks"
    res = requests.get(chart_url)
    print(res.json())
    tracks = []
    for track in res.json()['data']:
        tracks.append({
            'id': track['id'],
            'title': track['title'],
            'artist_name': track['artist']['name'],
            'artist_img': track['artist']['picture_medium'],
            'preview': track['preview']
        })
    return tracks
