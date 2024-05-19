from django.urls import path
from user.api import views


urlpatterns = [
    path('user/', views.UserList.as_view(), name='user_list'),
]
