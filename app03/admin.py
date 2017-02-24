from django.contrib import admin

# Register your models here.

from app03 import models
admin.site.register(models.Host)
admin.site.register(models.HostGroup)
admin.site.register(models.UserProfile)
admin.site.register(models.IDC)