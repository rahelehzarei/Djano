from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'first_app/home.html')

def search(request):
    return render(request,'first_app/search.html')

def about(request):
    return render(request,'first_app/about.html')

def index(request):
    playlist_list={"playlists":{'1': {'Love Lies', 'raheleh', 'Love Lies', 3.21}, '2': {'Rise', 'Jack and Jonas', 'Blue', 3.14}}}
    return render(request,'first_app/index.html', context=playlist_list)
