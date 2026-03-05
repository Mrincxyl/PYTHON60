from django.shortcuts import render

# Create your views here.
def Blogs(request):
    return render(request, 'allblogs.html')

def Create(request):
    return render(request, 'create.html')