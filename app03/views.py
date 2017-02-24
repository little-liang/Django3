from django.shortcuts import render
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
    return render(request, 'index.html')

def host(request):
    return render(request, 'host.html')

def asset(request):
    return render(request, 'asset.html')

def audit(request):
    return render(request, 'audit.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    else:

        print(request.POST)
    return render(request, 'login.html')