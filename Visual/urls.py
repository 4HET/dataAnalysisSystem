from django.urls import path, re_path
from Visual import views

urlpatterns = [
    path('visual/', views.visual),
]
