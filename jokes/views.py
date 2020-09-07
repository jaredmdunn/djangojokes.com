import json

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from .forms import JokeForm

from .models import Joke, JokeVote

class JokeCreateView(SuccessMessageMixin, CreateView):
    model = Joke
    form_class = JokeForm
    success_message = "Joke created."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeDeleteView(UserPassesTestMixin, DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Joke deleted.')
        return result

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class JokeDetailView(DetailView):
    model = Joke

class JokeListView(ListView):
    model = Joke

class JokeUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Joke
    form_class = JokeForm
    success_message = "Joke updated."

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

    def vote(request, slug):
        user = request.user
        joke = Joke.objects.get(slug=slug)
        data = json.loads(request.body)

        vote = data['vote']
        likes = data['likes']
        dislikes = data['dislikes']

        if user.is_anonymous:
            msg = 'Sorry, you have to be logged in to vote.'
        else:
            if JokeVote.objects.filter(user=user, joke=joke).exists():
                joke_vote = JokeVote.objects.get(user=user, joke=joke)

                if joke_vote.vote == vote:
                    msg = 'Right. You told us already. Geez.'
                else: 
                    joke_vote.vote = vote
                    joke_vote.save()

                    if vote == -1:
                        likes -= 1
                        dislikes += 1
                        msg = "Don't like it after all, huh? Ok. Noted."
                    else:
                        likes += 1
                        dislikes -= 1
                        msg = 'Grown on you, has it? Ok. Noted.'

            else:
                joke_vote = JokeVote(user=user, joke=joke, vote=vote)
                joke_vote.save()

                if vote == -1:
                    likes -= 1
                    dislikes += 1
                    msg = "Sorry you didn't like the joke."
                else:
                    likes += 1
                    dislikes -= 1
                    msg = 'Yeah, good one, right?'

        response = {
            'msg' : msg,
            'likes' : likes,
            'dislikes' : dislikes
        }
        return JsonResponse(response)