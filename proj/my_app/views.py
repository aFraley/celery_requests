from django.views.generic.list import ListView
from .models import Tweet


class TweetListView(ListView):
    model = Tweet
    template_name = 'my_app/tweet_list.html'

    def get_queryset(self):
        return Tweet.objects.all()

