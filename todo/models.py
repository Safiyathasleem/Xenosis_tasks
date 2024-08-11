from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField() # Field to store the title of the to-do item
    completed = models.BooleanField(default=False)  # Field to mark the item as completed or not

    def __str__(self) -> str:
        return self.title  # Display the title in the admin panel and elsewhere

