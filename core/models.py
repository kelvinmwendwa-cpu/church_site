from django.db import models
from django.contrib.auth.models import User

# Announcements
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

# Sermons
class Sermon(models.Model):
    title = models.CharField(max_length=200)
    speaker = models.CharField(max_length=120)
    date = models.DateField()
    series = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='sermons/audio/', blank=True, null=True)
    video_url = models.URLField(blank=True)  # YouTube/Facebook link
    notes_pdf = models.FileField(upload_to='sermons/notes/', blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} ({self.date})"

# Photos
class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title or f"Photo {self.id}"
