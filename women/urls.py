from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('cats/<int:cat_id>/', views.categories),
]
