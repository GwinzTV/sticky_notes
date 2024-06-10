# sticky_notes_app/forms.py
"""
Forms for the Sticky Notes App.

This module defines the forms used for creating and updating Note objects in
the Sticky Notes App. It includes the NoteForm class, which is a ModelForm for
the Note model. This form allows users to input data for the title and content
fields of a note.
"""
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating Note objects.

    Fields:
    - title: CharField for the note title.
    - content: TextField for the note content.

    Meta class:
    - Defines the model to use (Note) and the fields to include in the
    form.

    :param forms.ModelForm: Django's ModelForm class.
    """
    class Meta:
        model = Note
        fields = ['title', 'content', 'author']
