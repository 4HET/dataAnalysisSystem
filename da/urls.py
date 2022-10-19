from django.urls import path, re_path
from da import views

urlpatterns = [
    path('dataAnalysis/', views.index),
    path('myData/', views.myData),
]
