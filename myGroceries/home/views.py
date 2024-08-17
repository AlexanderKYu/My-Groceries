from django.shortcuts import render, redirect
from user.models import User

def home(request):
    if request.session.get('user_data', None):
        userFname = request.session['user_data']['given_name']
        userEmail = request.session['user_data']['email']
        if not User.objects.filter(email=userEmail):
            user = User(fname = userFname, email = userEmail)
            user.save()
        userId = User.objects.filter(email=userEmail).values('id')[0]['id']
        context = {}
        context['userId'] = userId
        return render(request, 'home.html', context)
    else:
        return redirect('sim/')