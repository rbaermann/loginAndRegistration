from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'loginandreg_app/index.html')

def reg(request):
    errors = Login.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        newLogin = Login.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        newLogin.save()
    return redirect('/success')

def log(request):
    errors = Login.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        login = Login.objects.get(email = request.POST['email'])
        request.session['login'] = login.id
        request.session['first_name'] = login.first_name
    return redirect('/success')

def success(request):
    if 'login' not in request.session:
        return redirect('/')
    context = {}
    context['first_name'] = request.session['first_name']
    return render(request, 'loginandreg_app/success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')