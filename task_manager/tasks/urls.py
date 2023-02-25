from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [
     path('', include('django.contrib.auth.urls')),
     path('register/', Register.as_view(), name='register'),
     path('', TaskView.as_view(), name='index'),
     path('create/', TaskView.as_view(), name='create'),
     path('update/<int:task_id>/', TaskUpdateView.as_view(), name='update'),
     path('delete/<int:task_id>/', TaskDeleteView.as_view(), name='delete'),

]
