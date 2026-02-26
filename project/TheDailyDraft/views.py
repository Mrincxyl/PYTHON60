from django.shortcuts import render

def MyHome(req):
    return render(req, 'home.html')

def About(req):
    return render(req, 'about.html')

def Login(request):
    return render(request, 'login.html')

def Register(request):
    return render(request, 'register.html')