from django.contrib import admin

# Register your models here.

from app03 import models
admin.site.register(models.Article)
admin.site.register(models.Category)
admin.site.register(models.UserProfile)
admin.site.register(models.ThumbUp)
admin.site.register(models.Comment)
admin.site.register(models.UserGroup)
