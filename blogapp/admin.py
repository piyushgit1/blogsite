from django.contrib import admin

from blogapp.models import User, Article, Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
