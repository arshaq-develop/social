from django.shortcuts import render
from socialApp.serializers import UserSerializer, UserProfileSerializer, PostSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from socialApp.models import UserProfile, PostModel
from rest_framework.decorators import action

# Create your views here.

class UserView(ModelViewSet):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class UserProfileView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
        
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)
    
    @action(methods=['POST'], detail=True)
    def add_follower(self, request, *args, **kwargs):
        profile_to_follow = UserProfile.objects.get(id=kwargs.get('pk'))
        user = request.user
        profile_to_follow.followers.add(user)
        return Response({'msg':'Followed'})
    
class PostView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user= self.request.user)
    
    
    @action(methods=['POST'], detail=True)
    def add_likes(self, request, *args, **kwargs):
        post_to_like = PostModel.objects.get(id = kwargs.get('pk'))
        user = request.user
        post_to_like.likes.add(user)
        return Response({'msg':'post like added'})
