from django.shortcuts import redirect, render, get_object_or_404
from .models import Task, Category
from .forms import TaskForm

def index_view(request):
    return render(request, "index.html", {})

def list_view(request, category_id):
    keyword = request.GET.get('keyword')
    user = request.user if request.user.is_authenticated else None
    tasks = Task.objects.all().filter(user=user)
    if keyword:
        tasks = Task.objects.filter(name__icontains = keyword)
    else:
        if category_id != 3:
            tasks = tasks.filter(category__id = category_id)    
    context = {
        'keyword': keyword,
        'tasks': tasks
    }
    return render(request, "list.html", context)




