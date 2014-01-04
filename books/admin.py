# coding:utf-8

from django.contrib import admin

# Register your models here.
from models import *

# string to html_safe
from django.utils.html import format_html

# 定義 Person Admin Class, 與這個 Person Admin 的 Configure
class PersonAdmin(admin.ModelAdmin):
	list_display=['id','first_name','last_name','myField']

	# 自定義的欄位, 可以用來放圖片或其他想要的資訊等
	def myField(self,obj):
		# 必須經過 format_html 主換, 不然會變成規避字
		return format_html( '<span>%s %s</span>'%(obj.first_name, obj.last_name) )

# 增加一個 Model 進去, 之後就可以在後台看到了
admin.site.register(Person, PersonAdmin)
