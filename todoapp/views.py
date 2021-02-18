from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UpdateForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.order_by('completd', 'due')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        #return redirect('/')
    context ={'tasks': tasks, 'form': form }
    return render(request, 'todoapp/list_task.html', context)


def update_task(request, id):
    tasks = Task.objects.get(id=id)
    form = UpdateForm(instance=tasks)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form': form , 'tasks':tasks}
    return render(request, 'todoapp/update_task.html', context)

def delete_task(request, id):
    tasks= Task.objects.get(id=id)
    if request.method == 'POST':
        tasks.delete()
        return redirect('/')

    context ={
        'tasks': tasks
    }
    return render(request, 'todoapp/delete_task.html', context)