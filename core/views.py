from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Announcement, Sermon, Photo
from .forms import AnnouncementForm, SermonForm, PhotoForm

# Home page
def home(request):
    latest_announcements = Announcement.objects.all()[:5]
    latest_sermons = Sermon.objects.all()[:5]
    return render(request, 'home.html', {
        'latest_announcements': latest_announcements,
        'latest_sermons': latest_sermons
    })

# Announcements list
def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements/list.html', {'announcements': announcements})

# Sermons list
def sermon_list(request):
    sermons = Sermon.objects.all()
    return render(request, 'sermons/list.html', {'sermons': sermons})

# Photo gallery
def photo_gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery/list.html', {'photos': photos})

# Support page
def support(request):
    return render(request, 'support.html')

# Authentication
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid credentials')
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

# Dashboard
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# Pastor/Admin create content
@login_required
@permission_required('core.add_announcement', raise_exception=True)
def announcement_create(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            ann = form.save(commit=False)
            ann.author = request.user
            ann.save()
            messages.success(request, 'Announcement published.')
            return redirect('announcement_list')
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/form.html', {'form': form})

@login_required
@permission_required('core.add_sermon', raise_exception=True)
def sermon_create(request):
    if request.method == 'POST':
        form = SermonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sermon added.')
            return redirect('sermon_list')
    else:
        form = SermonForm()
    return render(request, 'sermons/form.html', {'form': form})

@login_required
@permission_required('core.add_photo', raise_exception=True)
def photo_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo uploaded.')
            return redirect('photo_gallery')
    else:
        form = PhotoForm()
    return render(request, 'gallery/form.html', {'form': form})
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode='payment',
            line_items=[{
                'price_data': {
                    'currency': 'usd',  # or 'kes' if you want Kenyan Shillings
                    'product_data': {'name': 'Church Support Donation'},
                    'unit_amount': 5000,  # amount in cents (5000 = $50.00)
                },
                'quantity': 1,
            }],
            success_url=request.build_absolute_uri('/') + '?status=success',
            cancel_url=request.build_absolute_uri('/give/') + '?status=cancel',
        )
        return redirect(session.url, code=303)
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=400)
