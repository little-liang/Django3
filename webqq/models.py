from django.db import models
from app03 import models as bbs_models

# Create your models here.

class QQGroup(models.Model):
    name = models.CharField(max_length=64)
    #关联同一张表多次，必须有related_name
    founder = models.ForeignKey(bbs_models.UserProfile)
    brief = models.TextField(max_length=1024, default='nothing....')
    admin = models.ForeignKey(bbs_models.UserProfile, related_name='group_admins')
    members = models.ManyToManyField(bbs_models.UserProfile, related_name='group_members')
    member_limit = models.IntegerField(default=200)

    def __str__(self):
        return self.name