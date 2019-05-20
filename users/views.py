from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout
from django.views import View

from users.forms import LoginForm



class LoginView(View):

    def get(self, request):

        if request.user.is_authenticated:
            return redirect('home')

        else:
            form = LoginForm()

        context = {'form': form}

        return render(request, 'users/login.html', context)



    def post(self, request):

        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get('usr')
            password = request.POST.get('pwd')

            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, 'Incorrect username / password')

            else:
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)

        context = {'form': form}

        return render(request, 'users/login.html', context)






class LogoutView(View):

    def get(self, request):
        django_logout(request)
        return redirect('login')