from django.urls import path
from .views import *
app_name = 'tasks'
urlpatterns = [
    path('', index_view, name = 'index'),
]