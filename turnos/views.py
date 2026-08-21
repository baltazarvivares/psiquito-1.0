from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')  # si pedís confirmación

        if password != password2:
            return render(request, 'turnos/register.html', {
                'error': 'Las contraseñas no coinciden'
            })

        if User.objects.filter(username=email).exists():
            return render(request, 'turnos/register.html', {
                'error': 'Ese email ya está registrado'
            })

        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        login(request, user)
        return redirect('turnos:agenda')

    return render(request, 'turnos/register.html')