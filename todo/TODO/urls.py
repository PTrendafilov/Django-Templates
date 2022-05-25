from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/task', views.create_task, name='create_task'),
    path('complete/<int:id>/', views.complete_task, name='complete_task'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('edit/<int:id>/task', views.edit_task, name='edit_task'),
]