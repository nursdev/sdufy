from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def playlist(request):
    return render(request, 'sdufy/playlist.html')


def signIn(request):
    return HttpResponse('signIn')

def signUp(request):
    return HttpResponse('signUp')

def favorite(request):
    return HttpResponse('favorite')