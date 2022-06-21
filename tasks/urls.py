from django.urls import path
from .views import *
app_name = 'tasks'
urlpatterns = [
    path('', index_view, name = 'index'),
    # path('list/', list_view, name = 'list'),
    path('list/<int:category_id>', list_view, name = 'list'),
    path('list/<int:category_id>/<int:task_id>', detail_view, name = 'detail'),
    path('list/<int:category_id>/<int:task_id>/complete', complete_view, name = 'detail'),
]
