from django.contrib import admin

# Register your models here.
from models import *

# 定義原本的 Admin Class
class AuthorAdmin(admin.ModelAdmin):pass

# 增加一個 Model 進去, 之後就可以在後台看到了
admin.site.register(Person, AuthorAdmin)
