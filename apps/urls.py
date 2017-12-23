from django.urls import path,re_path,include
from . import views


app_name='apps'

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('user/<int:pk>/', views.profile, name='profile'),
    path('user/<int:pk>/followings/', views.followings, name='followings'),
    path('user/<int:pk>/followers/', views.followers, name='followers'),
    path('follow/<int:pk>/', views.follow, name='follow'),
    path('tweet_new/', views.tweet_new, name='tweet_new'),
    path('tweet_detail/<int:pk>/', views.tweet_detail, name='tweet_detail'),
    path('like/<int:pk>/', views.like, name='like'),
    path('<int:pk>/likes/', views.likes, name='likes'),
]
