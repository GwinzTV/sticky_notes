# sticky_notes_app/admin.py

"""
Admin configuration for Sticky Notes App.

This module defines how the models in the Sticky Notes App are displayed and
managed in the Django admin interface. It registers the Note and Author models
to make them editable via the admin interface.

Classes:
    None

Functions:
    None

Attributes:
    None
"""

from django.contrib import admin
from .models import Note
from .models import Author

# Register your models here.

# Note model
admin.site.register(Note)

# Author model
admin.site.register(Author)
