"""
URL configuration for use_external_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from .views import HomeView, LoginView, SignUpView, AccountView, LogoutView, AnimeView, SportsView, MarvelView, FoodView, LikeView, UnlikeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('account/', AccountView.as_view(), name="account"),
    path('logout/', LogoutView, name="logout"),

    path('anime/', AnimeView.as_view(), name="anime"),
    path('sports/', SportsView.as_view(), name="sports"),
    path('marvel/', MarvelView.as_view(), name="marvel"),
    path('food/', FoodView.as_view(), name="food"),

    path('like/', LikeView.as_view()),
    path('unlike/', UnlikeView.as_view())

]