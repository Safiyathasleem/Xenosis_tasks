#!/usr/bin/env python
# coding: utf-8

# # unit Testing
# 
# 

# In[ ]:


from django.test import TestCase
from .models import TodoItem

class TodoItemModelTest(TestCase):
    def setUp(self):
        self.todo = TodoItem.objects.create(title="Test Task", completed=False)

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, "Test Task")
        self.assertFalse(self.todo.completed)

    def test_string_representation(self):
        self.assertEqual(str(self.todo), "Test Task")


# In[ ]:


from django.test import TestCase
from .forms import TodoItemForm

class TodoItemFormTest(TestCase):
    def test_form_validity(self):
        form_data = {'title': 'Test Task', 'completed': False}
        form = TodoItemForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalidity(self):
        form = TodoItemForm(data={})  # Missing required fields
        self.assertFalse(form.is_valid())


# In[ ]:


from django.test import TestCase
from django.urls import reverse
from .models import TodoItem

class TodoItemViewTest(TestCase):
    def setUp(self):
        self.todo = TodoItem.objects.create(title="Test Task", completed=False)

    def test_view_status_code(self):
        response = self.client.get(reverse('todo_list'))  # Replace 'todo_list' with your view name
        self.assertEqual(response.status_code, 200)

    def test_view_template_used(self):
        response = self.client.get(reverse('todo_list'))
        self.assertTemplateUsed(response, 'todo_list.html')  # Replace with your template


# # Integration Testing
# 

# In[ ]:


from django.test import TestCase
from django.urls import reverse
from .models import TodoItem

class TodoItemIntegrationTest(TestCase):
    def setUp(self):
        self.todo = TodoItem.objects.create(title="Test Task", completed=False)

    def test_todo_item_creation_and_display(self):
        # Create a new Todo item
        response = self.client.post(reverse('todo_create'), {'title': 'New Task', 'completed': False})
        self.assertEqual(response.status_code, 302)  # Redirect status

        # Check that the new Todo item appears in the list
        response = self.client.get(reverse('todo_list'))
        self.assertContains(response, 'New Task')


# In[ ]:


python manage.py test

