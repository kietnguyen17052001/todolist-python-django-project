from asyncio import tasks
import datetime
from django.shortcuts import redirect, render, get_object_or_404
from .models import Task, Category
from .forms import TaskForm
def index_view(request):
    return render(request, "index.html", {})
        
def list_view(request, category_id):
    keyword = request.GET.get('keyword')
    sort = request.GET.get('sort')
    user = request.user if request.user.is_authenticated else None
    tasks = Task.objects.all()
    if keyword:
        tasks = tasks.filter(name__icontains = keyword)
    if category_id != 3:
        tasks = tasks.filter(category__id = category_id)
        dt = datetime.datetime.today()
        tasks = tasks.filter(createdAt__contains = datetime.date(dt.year, dt.month, dt.day))
    tasks = tasks.filter(user=user)
    if sort=="1":
        tasks = tasks.order_by('name').values()
    if sort=="2":
        tasks = tasks.order_by('complete').values()
    count_complete = tasks.filter(complete = True).count()
    count_incomplete = tasks.filter(complete = False).count()
    context = {
        'keyword': keyword,
        'category_id': category_id,
        'tasks': tasks,
        'count_complete': count_complete,
        'count_incomplete': count_incomplete,
        'typesort': sort,
        "category_id": category_id,
        'form':TaskForm()
    }
    return render(request, "list.html", context)
    

def add_task(request,category_id):
    keyword = request.GET.get('keyword')
    sort = request.GET.get('sort')
    if keyword == "None":
        keyword = ''
    if sort == "None":
        sort = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            user = request.user if request.user.is_authenticated else None
            task = Task(name=request.POST["name"], user=user,category=Category.objects.get(id=category_id))
            now = datetime.datetime.now()
            task.createdAt = now
            task.updatedAt = now
            task.save()
            return redirect(f"/list/{category_id}?keyword={keyword}&sort={sort}")

    return redirect("tasks:index")    
def detail_view(request, category_id, task_id):
    keyword = request.GET.get('keyword')
    sort = request.GET.get('sort')
    if keyword == "None":
        keyword = ''
    if sort == "None":
        sort = ''
    task = Task.objects.get(id=task_id)
    user = request.user if request.user.is_authenticated else None
    tasks = Task.objects.all()
    if keyword:
        tasks = Task.objects.filter(name__icontains = keyword)
    if category_id != 3:
        tasks = tasks.filter(category__id = category_id)
        dt = datetime.datetime.today()
        tasks = tasks.filter(createdAt__contains = datetime.date(dt.year, dt.month, dt.day))    
    tasks = tasks.filter(user=user)
    if sort=="1":
        tasks = tasks.order_by('name').values()
    if sort=="2":
        tasks = tasks.order_by('complete').values()
    count_complete = tasks.filter(complete = True).count()
    count_incomplete = tasks.filter(complete = False).count()
    context = {
        'keyword': keyword,
        'task': task,
        'tasks': tasks,
        'category_id': category_id,
        'count_complete': count_complete,
        'count_incomplete': count_incomplete,
        'typesort': sort,
        'form':TaskForm()
    }
    return render(request, 'list.html', context)

def complete_view(request, category_id, task_id):
    task = Task.objects.get(id=task_id)
    sort = request.GET.get('sort')
    keyword = request.GET.get('keyword')
    if keyword == "None":
        keyword = ''
    if sort == "None":
        sort = ''
    task.complete = not task.complete
    task.save()

    return redirect(f"/list/{category_id}?keyword={keyword}&sort={sort}")


def update_view(request, category_id, task_id):
    task = get_object_or_404(Task, id=task_id)
    sort = request.GET.get('sort')
    keyword = request.GET.get('keyword')
    if request.method == "POST":
        task.name=request.POST["name"]
        try:
            task.complete=request.POST["iscomplete"]
        except KeyError:
            task.complete=False
        task.updatedAt = datetime.datetime.now()
        task.save()
        return redirect(f"/list/{category_id}?keyword={keyword}&sort={sort}")
    
def delete_view(request,category_id,task_id):
    sort = request.GET.get('sort')
    keyword = request.GET.get('keyword')
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect(f"/list/{category_id}?keyword={keyword}&sort={sort}")
