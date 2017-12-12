from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
]
