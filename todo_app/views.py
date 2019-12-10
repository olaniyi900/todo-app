from django.shortcuts import render
from .forms import TodoForm
from .models import Todo
from django.http import HttpResponseRedirect




def home(request):
    return render(request, 'base.html')


def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo.objects.create(name=form.cleaned_data['name'])
            return HttpResponseRedirect('/todo_app/index/')

    else:
        form = TodoForm()
        todos = Todo.objects.all()
        context = {'form': form, 'todos': todos}
        return render(request, 'todo_app/index.html', context)


def removeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return HttpResponseRedirect('/todo_app/index/')