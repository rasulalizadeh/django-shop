from django import forms
from django.forms import ModelForm
from .models import User


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'username', 'email', 'password']
    # nickname = forms.CharField(label='Nickname', max_length=100, required=False)
    # username = forms.CharField(label='Username', max_length=100)
    # email = forms.EmailField(label='Email', max_length=100)
    # password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
