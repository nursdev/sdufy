from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    musics = Music.objects.all()
    context = {
        "musics" : musics
    }
    return render(request, 'sdufy/home.html',context)