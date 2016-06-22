from celery import shared_task
import tweepy

from .models import Tweet
from django.db import IntegrityError

CONSUMER_KEY = 'Vp7FVQLSwESvE9oTQruw0TnhW'
CONSUMER_SECRET = 'miy6EsGklNYxAaVn37vTjAVGwP0c67IOyuY71AAyL1p2Ba4VPN'
ACCESS_TOKEN = '1952022900-5WAHk6l5d3GllFtqDPaucSpnraIokE6hU7aBxNJ'
ACCESS_TOKEN_SECRET = 'ekONOf6QxJG6Lq3k2kznfQ16x12BGm909wckYFcP8SlYZ'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


@shared_task(name='get_tweets')
def get_tweets():
    """Get some tweets from the twitter api and store them to the db."""
    db_tweets = Tweet.objects.all()
    max_id = min([tweet.tweet_id for tweet in db_tweets])
    tweets = api.search(
        q='#python',
        max_id=max_id,
        count=100
    )
    tweets_date = [tweet.created_at for tweet in tweets]
    tweets_id = [tweet.id for tweet in tweets]
    tweets_text = [tweet.text for tweet in tweets]

    for i, j, k in zip(tweets_date, tweets_id, tweets_text):
        try:
            Tweet.objects.create(
                tweet_date=i,
                tweet_id=j,
                tweet_text=k,
            )
        except IntegrityError:
            pass
