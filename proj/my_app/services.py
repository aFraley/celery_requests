import requests
from requests_oauthlib import OAuth1


CONSUMER_KEY = 'Vp7FVQLSwESvE9oTQruw0TnhW'
CONSUMER_SECRET = 'miy6EsGklNYxAaVn37vTjAVGwP0c67IOyuY71AAyL1p2Ba4VPN'
ACCESS_TOKEN = '1952022900-5WAHk6l5d3GllFtqDPaucSpnraIokE6hU7aBxNJ'
ACCESS_TOKEN_SECRET = 'ekONOf6QxJG6Lq3k2kznfQ16x12BGm909wckYFcP8SlYZ'

auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23python&count=1'
