from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

def home(request):
    if request.session.get('user_data', None):
        return render(request, 'home.html')
    else:
        return redirect('sim/')