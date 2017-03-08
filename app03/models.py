from django.db import models

from django.contrib.auth.models import User
# Create your models here.

#开始建表了，这个项目是为了设计bbs论坛的表结构

class Article(models.Model):
    title = models.CharField(max_length=64)          #文章标题
    category = models.ForeignKey('Category')         #板块与文章是一对多关系，从文章表角度来看，这个是多对一
    content = models.TextField(max_length=100000)     #文章内容是不固定的，也就是会很多，这个不填是想多少就多少
    author = models.ForeignKey('Userprofile')         #作者与文章也是多对一关系
    #thumb_up = models.ForeignKey('ThumbUp', blank=True)     #点赞 和 文章是多对一关系,这里其实错了，不能多对一，只能一对多
    #comments = models.ManyToManyField('Comment', blank=True)  ##点赞 和 文章是多对一关系,这里其实错了，不能多对一，只能一对多
    head_img = models.ImageField(upload_to='static/imgs/uploadCom')
    publish_date = models.DateTimeField(auto_now_add=True)  #文章创建时间是固定的，自动填写
    summary = models.CharField(max_length=500)  ##文章索引内容

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)       #板块名字
    admins = models.ManyToManyField('UserProfile')          #版主信息，版主管理多个板块，板块有多个版主
    def __str__(self):
        return self.name

class ThumbUp(models.Model):
    artile = models.ForeignKey('Article')    ##一个文章可以有多个赞
    user = models.ForeignKey('UserProfile')    ##一个用户可以点多个赞
    date = models.DateTimeField(auto_now_add=True) ##点赞的时间

    def __str__(self):
        return self.artile.title            #这个返回了article表的数据

class Comment(models.Model):
    artile = models.ForeignKey('Article')    ##一个评论可以有多个赞
    comments_title = models.CharField(max_length=32)  ##评论标题
    user = models.ForeignKey('UserProfile')    ##一个评论可以点多个赞
    comments = models.TextField(max_length=1024) ##评论内容很多
    date = models.DateTimeField(auto_now_add=True)  ##评论的时间

    ###这里有个多级评论，就是几楼几楼那种，你可以评论几楼，这样评论与评论之家，就有了关联,
    ##这里就成自关联！！！自关联必须加related_name

    ##这里两个blank null为 True，意思就是 admin前端 界面 不让为空，数据库存储时不让为空
    parent_comment = models.ForeignKey('Comment', blank=True, null=True, related_name='pid')

    def __str__(self):
        return self.comments_title


class UserProfile(models.Model):
    user = models.OneToOneField(User)                   #继承系统自带用户表,一对一关系
    name = models.CharField(max_length=32)      #名字可以重名
    user_groups = models.ManyToManyField('UserGroup')

    friends = models.ManyToManyField('self', blank=True, related_name='my_friends')


    def __str__(self):
        return self.name

class UserGroup(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name