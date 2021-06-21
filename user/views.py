from django.shortcuts import render
from .models import User
from django.contrib import messages

# Create your views here.
def list_users(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username, '', password)
        messages.success(request, 'User registered.')

    return render(request, 'users_table.html')