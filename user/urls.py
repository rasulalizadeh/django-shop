from django.urls import path
from .views import list_users, remove_user, login_user, register_user, logout_user

urlpatterns = [
    path('users', list_users, name='users'),
    path('users/login', login_user, name='users.login'),
    path('users/logout', logout_user, name='users.logout'),
    path('users/register', register_user, name='users.register'),
    path('users/<int:id>', remove_user, name='users.remove'),
]