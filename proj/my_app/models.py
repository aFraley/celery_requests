from django.db import models


class Tweet(models.Model):
    tweet_date = models.DateTimeField()
    tweet_id = models.CharField(max_length=50, unique=True)
    tweet_text = models.TextField()

    def __str__(self):
        return str(self.tweet_date) + '  |  ' + str(self.tweet_id)
