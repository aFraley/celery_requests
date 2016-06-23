from django.test import TestCase
from datetime import datetime

from .models import Tweet


class TweetTest(TestCase):
    def setUp(self):
        Tweet.objects.create(
            tweet_id=4321,
            tweet_date=datetime.now(),
            tweet_source='Center of the Universe',
            tweet_favorite_cnt=0,
            tweet_retweet_cnt=12,
            tweet_text='Testing, testing!'
        )