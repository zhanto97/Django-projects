from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import TodoForm
from .models import Todo


def index(request):
	todo = Todo.objects.order_by('id')
	form = TodoForm()

	context = {
		'todo': todo,
		'form': form
	}
	return render(request, 'todo/index.html', context)

@require_POST
def addNewTodo(request):
	form = TodoForm(request.POST)

	if form.is_valid():
		new_todo = Todo(todotext = request.POST['text'])
		new_todo.save()

	return redirect('index')

def completeTodo(request, todo_id):
	todo = Todo.objects.get(pk = todo_id)
	todo.complete = True
	todo.save()

	return redirect('index')

def deleteTodo(request):
	Todo.objects.filter(complete__exact = True).delete()

	return redirect('index')

def incompleteTodo(request, todo_id):
	todo = Todo.objects.get(pk = todo_id)
	todo.complete = False
	todo.save()

	return redirect('index')
