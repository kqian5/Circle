from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password',)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

