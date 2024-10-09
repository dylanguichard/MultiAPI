from typing import Any
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .like import getAllLikes
from .sports import getTeams
from .anime import getAnimes
from .food import getFood
from .marvel import getCharacter


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        print(user)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class SignUpForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
    )
    email = forms.EmailField(initial="dylan.guichard.78@gmail.com")


class SignUpView(FormView):
    template_name = "signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            user.save()
            login(self.request, user)
        return super().form_valid(form)


class AccountView(TemplateView):
    template_name = "account.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        likes = getAllLikes(self.request)
        print('Likes :', likes)
        likedSportsId = likes.filter(
            el_type='team').values_list('el_id', flat=True)
        likedFoodId = likes.filter(
            el_type='food').values_list('el_id', flat=True)
        likedMarvelId = likes.filter(
            el_type='marvel').values_list('el_id', flat=True)
        likedAnimeId = likes.filter(
            el_type='anime').values_list('el_id', flat=True)

        context['teams'] = []
        context['animes'] = []
        context['products'] = []
        context['characters'] = []

        print(likedSportsId)
        print(likedFoodId)
        print(likedMarvelId)
        print(likedAnimeId)

        teams = getTeams(self)
        for team in teams:
            if str(team['id']) in likedSportsId:
                context['teams'].append(team)

        animes = getAnimes(self.request)
        for anime in animes:
            if str(anime['id']) in likedAnimeId:
                context['animes'].append(anime)

        food = getFood()
        for product in food:
            if str(product['id']) in likedFoodId:
                context['products'].append(product)

        # marvel = getCharacter(self.request)
        # for character in marvel:

        #     if str(character['id']) in likedMarvelId:
        #         print(character)
        #         context['characters'].append(character)

        return context


def LogoutView(request):
    logout(request)
    return redirect("home")
