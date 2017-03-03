from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app03 import models, utils
# Create your views here.


def index(request):
    articles = models.Article.objects.all().order_by('publish_date')


    return render(request, 'index.html', {
        'articles': articles
    })


def article(request,article_id):
    #文章随便写是找不到的
    err_msg = ''
    try:
        article_obj = models.Article.objects.get(id=article_id)
    except BaseException as e:
        err_msg = str(e)

    return render(request, 'article.html', {
        'article': article_obj,
        'err_msg': err_msg
    })

def create_article(request):

    if request.method == 'GET':
        return render(request, 'create_article.html')
    elif request.method == 'POST':
        print(request.FILES)

        #为了bbs的创建，修改（多次），删除等，专门写一个类来处理
        #放在utlis中，utlis在APP中

        bbs_generater = utils.ArticleGen(request)
        res = bbs_generater.create()
        html_ele = ''' Your article [ <a href='/article/%s'>%s</a> ] has been created sucessfully''' % (res.id, res.title)

        return HttpResponse(html_ele)




def host(request):
    return render(request, 'article.html')

def asset(request):

    return render(request, 'create_article.html')


def audit(request):
    return render(request, 'audit.html')

def acc_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None: #pass authentication
            login(request, user)
            return HttpResponseRedirect('/')
        else: ##密码不对
            return render(request, 'login.html', {
                'login_error': 'Worng username or password',
            })

    else:
        return render(request, 'login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect("/")