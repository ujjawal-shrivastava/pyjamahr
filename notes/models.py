from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    pinned = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="note_images/", blank=True, null=True)
    background_color = models.CharField(max_length=20, blank=True, null=True)
