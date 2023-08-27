from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Task

# Create your views here.


def TaskListView(request):
    tasks = get_list_or_404(Task)
    return render(request, "tasks_list.html", context={"tasks": tasks})


def TaskCreateView(request):
    pass


def TaskUpdateView(request, task_id):
    pass


def TaskDeleteView(request, task_id):
    pass
