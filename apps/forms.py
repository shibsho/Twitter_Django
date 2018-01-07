from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class TweetForm(forms.ModelForm):

	class Meta:
		model = Tweet
		fields = ('text',)


class RegisterForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username']
		self.fields['password1']
		self.fields['password2']