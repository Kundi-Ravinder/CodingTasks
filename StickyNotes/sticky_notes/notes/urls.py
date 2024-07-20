from django.urls import path
from .views import get, get_all, create, update, delete

""" Setting Url path for different pages"""
urlpatterns = [
    path('', get_all, name ='notes'),
    path('<int:pk>/', get , name = 'note'),
    path('new/', create , name ='create_note'),
    path('<int:pk>/edit', update, name = 'update_note'),
    path('<int:pk>/delete', delete, name = 'delete_note')
    ]

