from rest_framework import serializers
from django.contrib.auth.models import User
from socialApp.models import UserProfile, PostModel, CommentModel


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = ['id','username', 'password', 'email']


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user = serializers.CharField(read_only = True)
    follower_list = UserSerializer(read_only = True, many=True)
    follower_count = serializers.IntegerField(read_only = True)
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'profile_pic', 'bio', 'gender', 'follower_list', 'follower_count']

class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only= True)
    user = serializers.CharField(read_only = True)
    likes_count = serializers.IntegerField(read_only = True)
    class Meta:
        model = PostModel
        fields = ['id', 'user', 'image', 'caption', 'likes_count']


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.CharField(read_only = True)
    user = serializers.CharField(read_only = True)
    class Meta:
        model = CommentModel
        fields = ['post','user','comment']

         