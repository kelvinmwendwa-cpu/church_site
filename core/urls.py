from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('sermons/', views.sermon_list, name='sermon_list'),
    path('gallery/', views.photo_gallery, name='photo_gallery'),
    path('give/', views.support, name='support'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard for pastor/admin
    path('dashboard/', views.dashboard, name='dashboard'),
    path('announcements/new/', views.announcement_create, name='announcement_create'),
    path('sermons/new/', views.sermon_create, name='sermon_create'),
    path('photos/new/', views.photo_upload, name='photo_upload'),

    # Donation checkout
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
]
