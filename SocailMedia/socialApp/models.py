from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media')
    bio = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    followers = models.ManyToManyField(User, related_name='followers')

    def follower_list(self):
        return self.followers.all()
    
    def follower_count(self):
        return self.followers.all().count()

class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    caption = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')

    def likes_count(self):
        return self.likes.all().count()
    

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)