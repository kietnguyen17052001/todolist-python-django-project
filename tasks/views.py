from django.shortcuts import redirect, render, get_object_or_404
from .models import Task, Category
from .forms import TaskForm

def index_view(request):
    return render(request, "index.html", {})

def list_view(request):
    keyword = request.GET.get('keyword')
    if keyword:
        tasks = Task.objects.filter(name__icontains = keyword)
    else:
        tasks = Task.objects.all()    
    context = {
        'keyword': keyword,
        'tasks': tasks
    }
    return render(request, "list.html", context)




