import hashlib

from django.shortcuts import render, redirect
from user.models import User

def family(request):
    if request.session.get('user_data', None):
        userFname = request.session['user_data']['given_name']
        userEmail = request.session['user_data']['email']
        if not User.objects.filter(email=userEmail):
            user = User(fname = userFname, email = userEmail)
            user.save()
        # userId = User.objects.filter(email=userEmail).values('id')[0]['id']
        familyCode = hashlib.sha256(userEmail.encode("utf-8")).hexdigest()
        context = {}
        context['familyCode'] = familyCode
        return render(request, 'family.html', context)
    else:
        return redirect('/sim/')
