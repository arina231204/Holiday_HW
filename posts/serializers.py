from rest_framework import serializers

from .models import Tweet, Comment


class TweetSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=225)
    text = serializers.CharField(max_length=225)
    created_at = serializers.DateTimeField(required=False)
    user_id = serializers.IntegerField(read_only=True)

    def save(self, **kwargs):
        print('creating new message')
        return super().save(**kwargs)

    def create(self, validated_data):
        tweet = Tweet.objects.create(
            title=validated_data['title'],
            text=validated_data['text'],
            user_id=validated_data['user_id']
        )
        return tweet


class CommentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=225)
    text = serializers.CharField(max_length=225)
    date = serializers.DateTimeField(required=False)
    tweet_id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    def save(self, **kwargs):
        print('creating new message')
        return super().save(**kwargs)

    def create(self, validated_data):
        tweet = Comment.objects.create(
            title=validated_data['title'],
            text=validated_data['text'],
            user_id=validated_data['user_id'],
            tweet_id=validated_data['user_id']
        )
        return tweet

    def update(self, instance, validated_data):
        title = validated_data.get('title')
        text = validated_data.get('text')
        if title:
            instance.title = title
        if text:
            instance.text = text
        instance.save()
        return instance
