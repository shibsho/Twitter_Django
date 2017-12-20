from django.urls import path,re_path,include
from . import views


app_name='apps'

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('user/<int:pk>/', views.profile, name='profile'),
    path('tweet_new/', views.tweet_new, name='tweet_new'),
    path('tweet_detail/<int:pk>/', views.tweet_detail, name='tweet_detail'),
    path('follow/<int:pk>/', views.follow, name='follow'),
]
