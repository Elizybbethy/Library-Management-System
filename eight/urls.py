from django.urls import path
from .views import RegisterUser, allUsers, homepage

urlpatterns = [
    path('', homepage, name="home"),
    path('user_add', RegisterUser, name="user_add"),
    path('all_users/', allUsers, name="all_users"),
]
