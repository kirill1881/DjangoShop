from django.conf.urls import include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('addItem/', views.add_item)
]