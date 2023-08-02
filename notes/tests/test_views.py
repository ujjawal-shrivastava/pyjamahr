from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from notes.models import Note

class NoteViewSetTest(APITestCase):

    def setUp(self):
        self.note = Note.objects.create(title='Test Note', content='This is a test note.')

    def test_list_notes(self):
        url = reverse('note-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_note(self):
        url = reverse('note-list')
        data = {'title': 'New Note', 'content': 'This is a new note.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 2)
    
    def test_retrieve_note(self):
        url = reverse('note-detail', args=[self.note.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.note.title)
    
    def test_update_note(self):
        url = reverse('note-detail', args=[self.note.id])
        data = {'title': 'Updated Note'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')
    
    def test_delete_note(self):
        url = reverse('note-detail', args=[self.note.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 0)
