"""
URL configuration for SocailMedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from socialApp import views
from rest_framework.authtoken import views as authview

router = DefaultRouter()
router.register('user', views.UserView, basename='user_view' )
router.register('profile', views.UserProfileView, basename='profile_view' )
router.register('post', views.PostView, basename='post_view' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token', authview.obtain_auth_token),


] + router.urls
