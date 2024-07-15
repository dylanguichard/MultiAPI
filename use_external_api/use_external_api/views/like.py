from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from use_external_api.models import Fav
import json


@method_decorator(csrf_protect, name='dispatch')
class LikeView(View):
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)

        fav = Fav()
        fav.username = request.user
        fav.el_id = body['elId']
        fav.el_type = body['type']
        fav.save()
        response = {
            "success": "Is it ?"
        }
        return JsonResponse(response, status=200)


@method_decorator(csrf_protect, name='dispatch')
class UnlikeView(View):
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)

        fav = Fav.objects.get(el_type=body['type'], el_id=body['elId'])
        fav.delete()
        response = {
            "success": "We delete it"
        }
        return JsonResponse(response, status=200)


def getAllLikes(request):
    return Fav.objects.filter(username=request.user)


def getLikesByType(request, tag):
    return Fav.objects.filter(username=request.user,
                              el_type=tag).values_list('el_id', flat=True)
