from django.urls import path
from .views import list_users

urlpatterns = [
    path('users', list_users, name='users')
]