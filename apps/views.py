from django.shortcuts import render
from .models import Tweet
from django.utils import timezone

# Create your views here.
def tweet_list(request):
	tweets = Tweet.objects.all().order_by('id')
	return render(request, 'apps/tweet_list.html', {'tweets': tweets})


