from django.shortcuts import render

# Create your views here.

def dashboard(request):

    #单独建立一个 templates webqq项目,里面放置对应的 webqq的html内容
    return render(request, 'webqq/dashboard.html')