from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout

from users.forms import LoginForm


def login(request):
    if request.user.is_authenticated:
        return redirect('home')



    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get('usr')
            password = request.POST.get('pwd')

            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, 'Incorrect username / password')

            else:
                django_login(request, user)
                return redirect('home')


    else:
        form = LoginForm()

    context = {'form': form}

    return render(request, 'users/login.html', context)


def logout(request):
    django_logout(request)
    return redirect('login')