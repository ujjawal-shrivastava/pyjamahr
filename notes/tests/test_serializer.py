from django.test import TestCase
from .models import Note
from .serializers import NoteSerializer


class NoteSerializerTest(TestCase):
    def setUp(self):
        self.note_data = {"title": "Test Note", "content": "This is a test note."}

    def test_valid_serializer(self):
        serializer = NoteSerializer(data=self.note_data)
        self.assertTrue(serializer.is_valid())

    def test_create_note(self):
        serializer = NoteSerializer(data=self.note_data)
        serializer.is_valid(raise_exception=True)
        note = serializer.save()
        self.assertEqual(note.title, "Test Note")
        self.assertEqual(note.content, "This is a test note.")

    def test_serializer_with_invalid_data(self):
        invalid_note_data = {"title": "", "content": ""}
        serializer = NoteSerializer(data=invalid_note_data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_field_required(self):
        serializer = NoteSerializer(data={"content": "Content is required."})
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors["title"][0], "This field is required.")

    def test_serializer_field_optional(self):
        serializer = NoteSerializer(
            data={"title": "Optional Title", "content": "Content is required."}
        )
        self.assertTrue(serializer.is_valid())
