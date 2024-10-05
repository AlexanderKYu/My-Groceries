from django.shortcuts import redirect, render

def inventory(request):
    if request.session.get('user_data', None):
        userFname = request.session['user_data']['given_name']
        userEmail = request.session['user_data']['email']
        context = {}
        return render(request, 'inventory.html', context)
    else:
        return redirect('sim/')