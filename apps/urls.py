from django.urls import path,include
from . import views

app_name='apps'
urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
]
