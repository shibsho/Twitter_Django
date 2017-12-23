from django.contrib import admin
from .models import Tweet, Relationship, Like
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'text',)
	list_display_links = ('id',)
admin.site.register(Tweet, TweetAdmin)


class RelationshipAdmin(admin.ModelAdmin):
	list_display = ('id', 'from_user', 'target_user',)
	list_display_links = ('id', 'from_user', 'target_user',)
admin.site.register(Relationship, RelationshipAdmin)


class LikeAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'tweet',)
	list_display_links = ('id', 'user', 'tweet',)
admin.site.register(Like, LikeAdmin)