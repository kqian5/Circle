from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'image', 'text',)

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'password': forms.PasswordInput
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

