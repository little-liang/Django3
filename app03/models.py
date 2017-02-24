from django.db import models

from django.contrib.auth.models import User
# Create your models here.


#开始建表了，第一个表为主机表,这里先不用做主键
class Host(models.Model):
    #char 64字节，唯一
    hostname = models.CharField(max_length=64, unique=True)
    ip_addr = models.GenericIPAddressField(unique=True)

    #默认值22
    port = models.IntegerField(default=22)
    system_type_choise = (
        ('linux', 'LINUX'),
        ('win32', 'WINDOWS')
    )
    system_type = models.CharField(choices=system_type_choise, max_length=32)
    #布尔值
    enaled = models.BooleanField(default=True)
    online_date = models.DateField()
    online_create_date = models.DateField(auto_now_add=True)

    #主机与主机组关系，多对多,这里是对应HostGroup表
    groups = models.ManyToManyField('HostGroup')

    #这里外键对应IDC表
    idc = models.ForeignKey('IDC')

    def __str__(self):
        return self.hostname

#这个是机房表
class IDC(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

#这个是主机组表
class HostGroup(models.Model):
    name = models.CharField(max_length=64, unique=True)


    def __str__(self):
        return self.name


#用户数配置表
class UserProfile(models.Model):

    #一一对应，这个只能对应一次，再来一次就是一对多了,这里继承了User表
    user = models.OneToOneField(User)
    name = models.CharField(max_length=64)

    #不是必选，可以为空
    host_groups = models.ManyToManyField('HostGroup', blank=True)

    ##这里可以直接管理主机，不是直接管理主机组
    hosts = models.ManyToManyField('Host', blank=True)

    def __str__(self):
        return self.name