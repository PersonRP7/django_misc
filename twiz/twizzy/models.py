from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.urls import reverse

class Tweet(models.Model):

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )

    title = models.CharField(
        max_length = 140
    )

    def __str__(self):
        return self.title

class Vote(models.Model):

    class Meta:
        abstract = True
        unique_together = ['user', 'tweet']

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )

    tweet = models.ForeignKey(
        Tweet,
        on_delete = models.CASCADE
    )

    created = models.DateTimeField(
        auto_now_add = True
    )

    @staticmethod
    def see_if_upvoted_or_downvoted(user_instance, tweet_instance, klass):
        if klass.objects.filter(
            user = user_instance,
            tweet = tweet_instance
        ):
            return True
        else:
            return False

    @staticmethod
    def delete_upvote_or_downvote(user_instance, tweet_instance, klass):
        instance = klass.objects.filter(
            user = user_instance,
            tweet = tweet_instance
        )
        instance.delete()

    @staticmethod
    def create_upvote_or_downvote(user_instance, tweet_instance, klass):
        try:
            klass.objects.create(
                user = user_instance,
                tweet = tweet_instance
            )
            return True
        except IntegrityError:
            return False

    @staticmethod
    def vote(user_instance, tweet_instance, klass):
        if isinstance(klass, Upvote):
            if Downvote.see_if_upvoted_or_downvoted(user_instance, tweet_instance, Downvote):
                Downvote.delete_upvote_or_downvote(user_instance, tweet_instance, Downvote)
                Upvote.create_upvote_or_downvote(user_instance, tweet_instance, Upvote)
            else:
                Upvote.create_upvote_or_downvote(user_instance, tweet_instance, Upvote)
        elif isinstance(klass, Downvote):
            if Upvote.see_if_upvoted_or_downvoted(user_instance, tweet_instance, Upvote):
                Upvote.delete_upvote_or_downvote(user_instance, tweet_instance, Upvote)
                Downvote.create_upvote_or_downvote(user_instance, tweet_instance, Downvote)
            else:
                Downvote.create_upvote_or_downvote(user_instance, tweet_instance, Downvote)

class Upvote(Vote):
    def __str__(self):
        return f"{self.user.username} upvoted {self.tweet} on {self.created}."

class Downvote(Vote):
    def __str__(self):
        return f"{self.user.username} downvoted {self.tweet} on {self.created}."

class Comment(Vote):
    
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'owner'
    )

    parent = models.ForeignKey(
        Tweet,
        on_delete = models.CASCADE,
        related_name = 'parent'
    )

    text = models.CharField(
        max_length = 140
    )

    def __str__(self):
        return self.text