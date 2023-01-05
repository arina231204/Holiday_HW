from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Author

User = get_user_model()


class Tweet(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __str__(self):
        return f'{self.user.username} - {self.title}'

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

User = get_user_model()
class Comment(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True,related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True,related_name='comment_dislikes')



    def __str__(self):
        return f'{self.text} - {self.title}'



