from django import forms
from .models import Announcement, Sermon, Photo

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'body']

class SermonForm(forms.ModelForm):
    class Meta:
        model = Sermon
        fields = ['title', 'speaker', 'date', 'series', 'description', 'audio_file', 'video_url', 'notes_pdf']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image', 'caption']
