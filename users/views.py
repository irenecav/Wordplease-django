from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST.get('usr')
        password = request.POST.get('pwd')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Incorrect username / password')

        else:
            return redirect('home')

    return render(request, 'users/login.html')