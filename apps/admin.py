from django.contrib import admin
from .models import Tweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'text',)
	list_display_links = ('id',)
admin.site.register(Tweet, TweetAdmin)