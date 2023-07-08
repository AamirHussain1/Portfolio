from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project, name='project'),
    path('add_project', views.add_project, name='add_project')
]
