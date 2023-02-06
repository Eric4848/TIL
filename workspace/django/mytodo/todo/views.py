from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.


def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo_list.html', {'todos': todos})


def post_list(request):
    if request.method == "GET":
        form = TodoForm()
        return render(request, 'todo_post.html', {'form': form})
    else:
        form = TodoForm(request.POST)
        if form.is_valid:
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo:todo_list')
        else:
            return redirect('todo:todo_list')


def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo_detail.html', {'todo': todo})


def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "GET":
        form = TodoForm(instance=todo)
        return render(request, 'todo_post.html', {'form': form})
    else:
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid:
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo:todo_list')
        else:
            return redirect('todo:todo_list')


def done_list(request):
    todos = Todo.objects.filter(complete=True)
    return render(request, 'done_list.html', {'todos': todos})


def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo:todo_list')


def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo:todo_list')
