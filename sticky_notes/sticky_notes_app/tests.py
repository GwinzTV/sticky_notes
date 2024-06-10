# sticky_notes_app/test.py
"""
Tests for the Sticky Notes App.

This module contains test cases for the functionality of the Sticky Notes App.
It includes various test cases to ensure that the models, views, forms, and
other components of the app work as expected.
"""

from django.test import TestCase
from django.urls import reverse
from .models import Note, Author


# Create your tests here.
class NoteModelTest(TestCase):
    def setUp(self):
        # Create an Author object
        author = Author.objects.create(name='Test Author')
        # Create a Note object for testing
        Note.objects.create(
            title='Test Note',
            content='This is a test note.',
            author=author
            )

    def test_note_has_title(self):
        # Test that a Note object has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        # Test taht a Note object has the expected content
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')


class NoteViewTest(TestCase):
    def setUp(self):
        # Create an Author object
        author = Author.objects.create(name='Test Author')
        # Create a Note object for testing views
        Note.objects.create(
            title='Test Note',
            content='This is a test note.',
            author=author
            )

    def test_note_list_view(self):
        # Test the note-list view
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        # Test the note-detail view
        note = Note.objects.get(id=1)
        response = self.client.get(reverse(
            'note_detail',
            args=[str(note.id)]
            ))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')
