from django.urls import path
from .views import *
app_name = 'tasks'
urlpatterns = [
    path('', index_view, name = 'index'),
    path('list/<int:category_id>', list_view, name = 'list'),
    path('list/<int:category_id>/task/<int:task_id>', update_view, name = 'update')
]