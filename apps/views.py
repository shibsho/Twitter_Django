from django.shortcuts import render, get_object_or_404
from .models import Tweet
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.
def tweet_list(request):
	tweets = Tweet.objects.all().order_by('id')
	return render(request, 'apps/tweet_list.html', {'tweets': tweets})

def profile(request,pk):
	user = get_object_or_404(User,pk=pk)
	tweets = Tweet.objects.filter(user=user)
	return render(request, 'apps/profile.html', {'user':user, 'tweets': tweets})
