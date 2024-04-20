from django.urls import path
from .views import *

urlpatterns = [
    path('api/app1/', App1ListView.as_view(), name='app1-list'),
    path('api/app1/<int:pk>/', App1DetailView.as_view(), name='app1-detail'),
]