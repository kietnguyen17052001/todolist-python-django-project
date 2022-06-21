from django.shortcuts import redirect, render, get_object_or_404
from .models import Task, Category
from .forms import TaskForm

def index_view(request):
    return render(request, "index.html", {})

def list_view(request, category_id):
    keyword = request.GET.get('keyword')
    user = request.user if request.user.is_authenticated else None
    tasks = Task.objects.all()
    if keyword:
        tasks = Task.objects.filter(name__icontains = keyword)
    if category_id != 3:
        tasks = tasks.filter(category__id = category_id)        
    tasks = tasks.filter(user=user)
    count_complete = tasks.filter(complete = True).count()
    count_incomplete = tasks.filter(complete = False).count()
    context = {
        'keyword': keyword,
        'category_id': category_id,
        'tasks': tasks,
        'count_complete': count_complete,
        'count_incomplete': count_incomplete,
    }
    return render(request, "list.html", context)

def update_view(request, category_id, task_id):
    task = Task.objects.get(id=task_id)
    task.complete = not task.complete
    task.save()
    return list_view(request, category_id)
    




