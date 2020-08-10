from django.views.generic import ListView, DetailView

from .models import Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeListView(ListView):
    model = Joke
