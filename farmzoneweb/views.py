# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def forum(request):
    return render(request, 'forum.html')


def listings(request):
    return render(request, 'listings.html')


def listing_single(request):
    return render(request, 'listings-single.html')


def login(request):
    return render(request, 'login.html')


def post_item(request):
    return render(request, 'postitem.html')


def profile(request):
    return render(request, 'profile.html')


def register(request):
    return render(request, 'register.html')
