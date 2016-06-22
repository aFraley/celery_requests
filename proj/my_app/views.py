from django.shortcuts import render
from .models import Tweet


def index(request):
    tweet_ids = Tweet.objects.all()
    return render(request, 'my_app/index.html', {'tweet_ids': tweet_ids})
