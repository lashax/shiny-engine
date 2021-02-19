from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from user.forms import UserRegistrationForm


def register(request: WSGIRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserRegistrationForm()
        return render(request, 'user/register.html', {'form': form})
    else:
        return redirect('home')

