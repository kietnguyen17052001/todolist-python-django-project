from django.urls import path
from .views import *
app_name = 'tasks'
urlpatterns = [
    path('', index_view, name = 'index'),
    path('list/<int:category_id>', list_view, name = 'list'),
    path('list/<int:category_id>/task/add', add_task, name = 'add_task'),
    path('list/<int:category_id>/task/<int:task_id>', detail_view, name = 'detail'),
    path('list/<int:category_id>/task/<int:task_id>/complete', complete_view, name = 'complete'),
    path('list/<int:category_id>/task/<int:task_id>/update', update_view, name='update'),
    path('list/<int:category_id>/task/<int:task_id>/delete', delete_view, name='delete'),
]
