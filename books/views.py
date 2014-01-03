# coding:utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # 這個是可以讓文字直接輸出的方法

def home(request):
	return HttpResponse('hello world by mysite.books.views.home')

# 給 model 用的
# 參考：https://docs.djangoproject.com/en/dev/topics/serialization/
from django.core import serializers
from models import *
def persons(request):
	#
	print Person.objects.all()
	#
	print serializers.serialize( "xml", Person.objects.all() )
	#
	# return HttpResponse(serializers.serialize( "xml", Person.objects.all() ), content_type="application/json")
	return HttpResponse(serializers.serialize( "json", Person.objects.all() ), content_type="application/json")			# 如果不是 application/json 會變成下載