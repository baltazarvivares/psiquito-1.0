from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
def Login(request):
    if request.method == 'POST':
        email    = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('turnos:agenda')
        else:
            return render(request, 'turnos/login.html', {
                'error': 'Email o contraseña incorrectos'
            })

    return render(request, 'turnos/login.html')
def Register(request):
    return render(request, 'turnos/register.html')
