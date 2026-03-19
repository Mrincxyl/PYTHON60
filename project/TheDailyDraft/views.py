from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def MyHome(req):
    return render(req, 'home.html')

@login_required(login_url='login')
def Pricing(req):
    return render(req, 'pricing.html')

