

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from todo.forms import TodoItemForm

def todo_list(request):
    items = TodoItem.objects.all()  # Fetch all to-do items
    return render(request, 'todo/todo_list.html', {'items': items})

def add_todo(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new to-do item to the database
            return redirect('todo_list')  # Redirect to the list of to-do items
    else:
        form = TodoItemForm()  # Create an empty form instance
    return render(request, 'todo/add_todo.html', {'form': form})

def edit_todo(request, pk):
    item = get_object_or_404(TodoItem, pk=pk)  # Fetch the to-do item by its primary key
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()  # Save the updated to-do item
            return redirect('todo_list')  # Redirect to the list of to-do items
    else:
        form = TodoItemForm(instance=item)  # Create a form instance with existing data
    return render(request, 'todo/edit_todo.html', {'form': form})

def toggle_complete(request, pk):
    item = get_object_or_404(TodoItem, pk=pk)  # Fetch the to-do item by its primary key
    item.completed = not item.completed  # Toggle the completed status
    item.save()  # Save the changes
    return redirect('todo_list')  # Redirect to the list of to-do items

