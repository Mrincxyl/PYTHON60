from django.shortcuts import render

def MyHome(req):
    return render(req, 'home.html')

def Pricing(req):
    return render(req, 'pricing.html')

