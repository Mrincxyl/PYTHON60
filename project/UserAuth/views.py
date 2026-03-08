from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('useremail')
        password = request.POST.get('password')

        
        alreadyExists = User.objects.filter(username=username).exists()

        if alreadyExists:
            messages.error(request, 'Username already exists')
            return render(request, 'register.html')
        else:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            messages.success(request, 'User registered successfully')
            return render(request, 'login.html')

    return render(request, 'register.html')

def Login(request):
    return render(request, 'login.html')

