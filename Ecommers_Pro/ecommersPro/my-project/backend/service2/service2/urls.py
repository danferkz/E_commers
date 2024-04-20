from django.urls import path
from .views import *

urlpatterns = [
    path('api/app2/', App2ListView.as_view(), name='app2-list'),
    path('api/app2/<int:pk>/', App2DetailView.as_view(), name='app2-detail'),
]