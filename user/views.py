from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from .forms import UserRegistrationForm, UserLoginForm
from rest_framework import viewsets
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


# Create your views here.
def list_users(request):
    users = User.objects.all()
    return render(request, 'users_table.html', {
        "register_form": UserRegistrationForm,
        "login_form": UserLoginForm,
        "users": users
    })


def remove_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('users')


def register_user(request):
    if request.method == 'POST':
        user_data = UserRegistrationForm(request.POST)
        if user_data.is_valid():
            try:
                user = User.objects.create_user(
                    user_data.cleaned_data['username'],
                    user_data.cleaned_data['email'],
                    user_data.cleaned_data['password']
                )
                if user is not None:
                    user.nickname = user_data.cleaned_data['nickname']
                    user.save()
                messages.success(request, 'User registered.')
            except:
                messages.error(request, 'Username already exists.')
        else:
            for error in user_data.errors:
                messages.error(request, error)

    return redirect('users')


def login_user(request):
    if request.method == 'POST':
        user_data = UserLoginForm(request.POST)
        if user_data.is_valid():
            try:
                user = authenticate(
                    username=user_data.cleaned_data['username'],
                    password=user_data.cleaned_data['password']
                )
                if user is not None:
                    login(request, user)
                    messages.success(request, 'User logged in.')
                else:
                    messages.error(request, 'Wrong username or password.')
            except:
                messages.error(request, 'Incorrect username or password.')
        else:
            for error in user_data.errors:
                messages.error(request, error)
    return redirect('users')


def logout_user(request):
    logout(request)
    return redirect('users')
