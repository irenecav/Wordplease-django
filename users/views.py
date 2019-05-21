from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout
from django.views import View
from django.views.generic import ListView

from users.forms import LoginForm, SignUpForm


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


class BlogListView(ListView):
    model = User

    template_name = 'users/blogs.html'


class SignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = SignUpForm()

        context = {'form': form}

        return render(request, 'users/signup.html', context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        context = {'form': form}

        return render(request, 'users/signup.html', context)
