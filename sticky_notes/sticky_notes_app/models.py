# sticky_notes_app/models.py
from django.db import models


# Create your models here.
class Note(models.Model):
    """
    Model representing a task manager sticky note.

    Fields:
    - title: CharField for the note title with a maximum length of 255
    characters.
    - content: TextField for the note content.
    - created_at: DateTimeField set to the current date and time when the
    note is created.

    Relationships:
    - author: ForeignKey representing the author of the note.

    Methods:
    - No specific methods are defined in this model.

    :param models.Model: Django's base model class.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Define a ForeignKey for the author's relationship
    author = models.ForeignKey('Author', on_delete=models.CASCADE,
                               null=True, blank=True)


class Author(models.Model):
    """
    Model representing teh author of the task manager sticky note

    Fields:
    - name: CharField for the author's name.

    Methods:
    - No specific methods are defined in this model.

    :param models.Model: Django's base model class.
    """
    name = models.CharField(max_length=255)
