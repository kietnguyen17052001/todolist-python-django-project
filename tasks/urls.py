from django.urls import path
from .views import *
app_name = 'tasks'
urlpatterns = [
    path('', index_view, name = 'index'),
    path('list/', list_view, name = 'list'),
]