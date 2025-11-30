from django.shortcuts import render, redirect
from .models import Task

def todo_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('todo_list')
    
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/todo_list.html', {'tasks': tasks})

def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('todo_list')