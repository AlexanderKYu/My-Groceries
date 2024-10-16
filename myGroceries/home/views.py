from django.shortcuts import render, redirect
from user.models import User
from groceries.models import Groceries
from groceries.models import Tags
from django.core.exceptions import ValidationError

def home(request):
    if request.session.get('user_data', None):
        userFname = request.session['user_data']['given_name']
        userEmail = request.session['user_data']['email']
        if not User.objects.filter(email=userEmail):
            try:
                user = User(fname = userFname, email = userEmail)
                user.save()
            except ValidationError:
                return redirect('/sim/')

        userId = User.objects.filter(email=userEmail).values('id')[0]['id']
        userInventory = Groceries.objects.filter(memberId=userId)
        context = {}
        context['userId'] = userId
        context['userInventory'] = userInventory

        return render(request, 'home.html', context)
    else:
        return redirect('/sim/')