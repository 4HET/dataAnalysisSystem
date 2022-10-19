from django.urls import path, re_path
from myData import views

urlpatterns = [
    path('myData/', views.index),
]
