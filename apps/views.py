from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet, Relationship
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import TweetForm

# Create your views here.
def tweet_list(request):
	tweets = Tweet.objects.all().order_by('-created_date')
	return render(request, 'apps/tweet_list.html', {'tweets': tweets})


def profile(request,pk):
	user = get_object_or_404(User, pk=pk)
	tweets = user.tweet_set.all().order_by('-created_date')
	following_relations = Relationship.objects.filter(from_user=user)
	followed_relations = Relationship.objects.filter(target_user=user)
	return render(request, 'apps/profile.html', {'user':user, 'tweets': tweets, 'following_relations': following_relations, 'followed_relations': followed_relations,})


def follow(request,pk):
	from_user = request.user
	target_user = User.objects.get(pk=pk)
	Relationship.objects.create(from_user=from_user, target_user=target_user)
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
	if request.method == "POST":
		tweet = get_object_or_404(Tweet,pk=pk)
		form = TweetForm(instance=tweet)
		tweet = form.save(commit=False)
		tweet.delete()
		return redirect('apps:profile', pk=request.user.pk)
	else:
		tweet = get_object_or_404(Tweet,pk=pk)
		form = TweetForm(instance=tweet)
		return render(request, 'apps/tweet_detail.html', {'form': form})
















