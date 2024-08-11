<<<<<<< HEAD
from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'completed']  # Fields to include in the form
=======
from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'completed']  # Fields to include in the form
>>>>>>> 9f802cbf9124b554e536ef9711edc4fa59e3d5a4
