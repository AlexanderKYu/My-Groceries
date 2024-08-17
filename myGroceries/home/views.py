from django.shortcuts import render, redirect
from user.models import User

def home(request):
    if request.session.get('user_data', None):
        userFname = request.session['user_data']['given_name']
        userEmail = request.session['user_data']['email']
        if not User.objects.filter(email=userEmail):
            user = User(fname = userFname, email = userEmail)
            user.save()
        return render(request, 'home.html')
    else:
        return redirect('sim/')