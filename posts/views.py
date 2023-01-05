from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.utils import json
from .models import Tweet, Comment
from .serializers import TweetSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework import authentication
from .mygenerics import MYAPIView, ListMixinAPI, CreateMixinAPI




class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

@login_required
def like_tweet(self, request):
    tweet = get_object_or_404(Tweet, id=request.POST.get('tweet_id'))
    is_liked = False
    if tweet.likes.filter(id=request.user.id).exists():
        tweet.likes.remove(request.user)
        is_liked = False
    else:
        tweet.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(tweet.get.absolute_url())
@login_required
def dislike_tweet(self, request):
    tweet = get_object_or_404(Tweet, id=request.POST.get('tweet_id'))
    is_liked = False
    if tweet.dislikes.filter(id=request.user.id).exists():
        tweet.dislikes.remove(request.user)
        is_liked = False
    else:
        tweet.dislikes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(tweet.get.absolute_url())


class TweetListAPIView(ListMixinAPI, CreateMixinAPI, MYAPIView):
    serializer_class = TweetSerializer
    model = Tweet

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

@login_required
def like_comment(self, request):
    comment = get_object_or_404(Comment, id=request.POST.get('tweet_id'))
    is_liked = False
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
        is_liked = False
    else:
        comment.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(comment.get.absolute_url())
@login_required
def dislike_comment(self, request):
    comment = get_object_or_404(Comment, id=request.POST.get('tweet_id'))
    is_liked = False
    if comment.dislikes.filter(id=request.user.id).exists():
        comment.dislikes.remove(request.user)
        is_liked = False
    else:
        comment.dislikes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(comment.get.absolute_url())


class CommentListAPIView(ListMixinAPI, CreateMixinAPI, MYAPIView):
    serializer_class = CommentSerializer
    model = Comment

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


#
#
