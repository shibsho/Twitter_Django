from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Tweet(models.Model):
	"""ツイート"""
	user = models.ForeignKey(User, on_delete=models.CASCADE,)
	text = models.TextField(max_length=140)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.text


class Relationship(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_u')
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='targeter')