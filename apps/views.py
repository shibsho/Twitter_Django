from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tweet, Relationship, Like
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import TweetForm
from django.db.models import Q



def tweet_list(request):
	tweets = Tweet.objects.all().order_by('-created_date')
	return render(request, 'apps/tweet_list.html', {'tweets': tweets})


def profile(request,pk):
	user = get_object_or_404(User, pk=pk)
	followings = Relationship.objects.filter(from_user=user).values('target_user')
	followers = Relationship.objects.filter(target_user=user).values('from_user')
	likes = Like.objects.filter(user=user)

	if Relationship.objects.filter(from_user=request.user, target_user=user).exists():
		following=True
	else:
		following=False

	if user == request.user:
		title = "timeline"
		following_users = User.objects.filter(pk__in=followings)
		tweets = Tweet.objects.filter(Q(user=user)|Q(user__in=following_users)).order_by('-created_date')
	else:
		title = str(user) + "のつぶやき"
		tweets = user.tweet_set.all().order_by('-created_date')
	tweets_count = tweets.count()
	
	return render(request, 'apps/profile.html', {'user':user, 'tweets': tweets, 'followings': followings, 'followers': followers, 'likes':likes, 'following': following, 'title': title,})


def followings(request,pk):
	user = get_object_or_404(User,pk=pk)
	followings = Relationship.objects.filter(from_user=user).values('target_user')
	following_users = User.objects.filter(pk__in=followings)
	return render(request, 'apps/followings.html', {'user': user, 'following_users': following_users, })


def followers (request,pk):
	user = get_object_or_404(User,pk=pk)
	followers = Relationship.objects.filter(target_user=user).values('from_user')
	follower_users = User.objects.filter(pk__in=followers)
	return render(request, 'apps/followers.html', {'user': user, 'follower_users': follower_users, })


@require_POST
def follow(request,pk):
	user = get_object_or_404(User, pk=pk)
	if 'follow' in request.POST:
		from_user = request.user
		target_user = User.objects.get(pk=pk)
		Relationship.objects.get_or_create(from_user=from_user, target_user=target_user)
	elif 'unfollow' in request.POST:
		from_user = request.user
		target_user = User.objects.get(pk=pk)
		relationship = Relationship.objects.filter(from_user=from_user, target_user=target_user)
		relationship.delete()
	return redirect('apps:profile', pk=pk)


def tweet_new(request):
	if request.method == "POST":
		form = TweetForm(request.POST)
		if form.is_valid():
			tweet = form.save(commit=False)
			tweet.user = request.user
			tweet.save()
			return redirect('apps:profile', pk=request.user.pk)
	else:
		form = TweetForm()
	return render(request, 'apps/tweet_new.html', {'form': form})


def tweet_detail(request,pk):
	tweet = get_object_or_404(Tweet,pk=pk)
	if Like.objects.filter(user=request.user, tweet=tweet).exists():
		liked=True
	else:
		liked=False	
	if request.method == "POST":
		tweet.delete()
		return redirect('apps:profile', pk=request.user.pk,)
	else:
		return render(request, 'apps/tweet_detail.html', {'tweet': tweet, 'liked':liked, })


@require_POST
def like(request,pk):
	tweet = Tweet.objects.get(pk=pk)
	if 'like' in request.POST:
		Like.objects.get_or_create(user=request.user, tweet=tweet)
	elif 'unlike' in request.POST:
		like = Like.objects.filter(user=request.user, tweet=tweet)
		like.delete()
	return redirect('apps:tweet_detail', pk=tweet.pk)


def likes(request,pk):
	user = User.objects.get(pk=pk)
	likes = Like.objects.filter(user=user).values('tweet')
	tweets = Tweet.objects.filter(pk__in=likes)
	return render(request, 'apps/likes.html', {'tweets':tweets, 'user':user, })











