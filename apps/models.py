from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Tweet(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,)
	text = models.TextField(max_length=140)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.text