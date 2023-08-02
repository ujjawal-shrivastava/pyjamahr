from django.test import TestCase
from .models import Note

class NoteModelTest(TestCase):

    def test_create_note(self):
        note = Note.objects.create(title='Test Note', content='This is a test note.')
        self.assertEqual(note.title, 'Test Note')
        self.assertEqual(note.content, 'This is a test note.')

    # Add more tests for other model methods and fields if needed
