from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm


# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'task_key': tasks,
        'form_key': form,
    }
    return render(request, 'task/list.html', context)


def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form_key': form,
    }
    return render(request, 'task/update.html', context)


def delete_task(request, task_id):
    item = Task.objects.get(id=task_id)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {
        'item_key': item,
    }
    return render(request, 'task/delete.html', context)
