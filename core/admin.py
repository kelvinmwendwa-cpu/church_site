from django.contrib import admin
from .models import Announcement, Sermon, Photo

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at')
    search_fields = ('title', 'body')
    list_filter = ('published_at',)

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'date', 'series')
    search_fields = ('title', 'speaker', 'series')
    list_filter = ('date',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'caption')
    search_fields = ('title', 'caption')
    list_filter = ('uploaded_at',)
