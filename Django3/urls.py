"""Django3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from app03 import views
from webqq import urls as chat_urls
from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^host/$', views.host, name='host'),
    url(r'^asset/$', views.asset, name='asset'),
    url(r'^audit/$', views.audit, name='audit'),
    url(r'^accounts/login/$', views.acc_login, name='login'),
    url(r'^logout/$', views.acc_logout, name='logout'),
    url(r'^article/(\d+)/$', views.article, name='article'),
    url(r'^create_article/$', views.create_article, name='create_article'),
    url(r'^chat/', include(chat_urls)),
]




