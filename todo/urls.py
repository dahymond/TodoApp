from django.urls import path, re_path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    re_path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
]