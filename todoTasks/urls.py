from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update_list/<int:pk>/', views.updateTask, name="update_list"),
    path('delete/<int:pk>/', views.deleteTask, name="delete"),
]
