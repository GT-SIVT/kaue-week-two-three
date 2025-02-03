from django.urls import path
from .views import register, user_list, login_view

urlpatterns = [
    path('register/', register, name='register'),
    path('list/', user_list, name='user_list'),
    path('login/', login_view, name='login'),
]
