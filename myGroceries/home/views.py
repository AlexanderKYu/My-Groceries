from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

def home(request):
    if request.session.get('user_data', None):
        fname = request.session['user_data']['given_name']
        email = request.session['user_data']['email']
        print(fname, email)
        return render(request, 'home.html')
    else:
        return redirect('sim/')