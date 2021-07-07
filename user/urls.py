from django.urls import path, include
from .views import list_users, remove_user, login_user, register_user, logout_user, UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('users/table', list_users, name='users'),
    path('users/login', login_user, name='users.login'),
    path('users/logout', logout_user, name='users.logout'),
    path('users/register', register_user, name='users.register'),
    path('users/<int:id>', remove_user, name='users.remove'),

    path('', include(router.urls))
]