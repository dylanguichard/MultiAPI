from typing import Any
from django.views.generic import TemplateView
import openfoodfacts
import requests
from .like import getLikesByType


class FoodView(TemplateView):
    template_name = "food.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # products = openfoodfacts.products.search('Nutella')['products']

        res = getFood()

        context['products'] = res
        context['likes'] = getLikesByType(
            request=self.request, tag="food")
        return context


def getFood():
    return requests.get(
        "https://world.openfoodfacts.net/api/v2/search?categories_tags=chocolates&page=24&page_size=24").json()['products']
