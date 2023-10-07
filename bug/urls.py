from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_bug/', views.create_bug, name='add_bug'),
    path('bug/<int:pk>/', views.view_bug, name='view_bug'),
]