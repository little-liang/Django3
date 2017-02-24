from django.shortcuts import render, HttpResponseRedirect
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

        user = authenticate(username=username, password=password)
        if user is not None: #pass authentication
            return HttpResponseRedirect('/')
        else: ##密码不对
            return render(request, 'login.html', {
                'login_error': 'Worng username or password',
            })

    else:
        return render(request, 'login.html')