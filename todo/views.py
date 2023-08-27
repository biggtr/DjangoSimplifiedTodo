from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Task

# Create your views here.


def TaskListView(request):
    tasks = get_list_or_404(Task)
    return render(request, "tasks_list.html", context={"tasks": tasks})


def TaskCreateView(request):
    form = TaskForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("task-list")
    else:
        form = TaskForm()
    return render(request, "task_create.html", context={"form": form})


def TaskUpdateView(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task-list")
    else:
        form = TaskForm(instance=task)
    return render(request, "task_update.html", context={"form": form})


def TaskDeleteView(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("task-list")
    return render(request, "task_delete.html", context={"task": task})
