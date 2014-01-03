# coding:utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # 這個是可以讓文字直接輸出的方法

def home(request):
	return HttpResponse('hello world by mysite.books.views.home')

# 給 model 用的
# 參考：https://docs.djangoproject.com/en/dev/topics/serialization/
from django.core import serializers
import json # 簡單的 json 轉換
from models import *

# 修飾 function 使用 GET / POST
from django.views.decorators.http import require_http_methods

# 引入 CRSF 豁免權
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt # 單一方法豁免 CRSF, 如果要完全關閉 CRSF 保護就 comment settings.py 內的 django.middleware.csrf.CsrfViewMiddleware
@require_http_methods(["GET", "POST"]) 	# 修飾可使用 GET / POST 預設只能使用 GET
def persons(request):
	if request.method=='GET':
		#
		print Person.objects.all()
		#
		print serializers.serialize( "xml", Person.objects.all() )
		#
		# return HttpResponse(serializers.serialize( "xml", Person.objects.all() ), content_type="application/json")
		return HttpResponse(serializers.serialize( "json", Person.objects.all() ), content_type="application/json")			# 如果不是 application/json 會變成下載

	elif request.method=='POST':
		row=Person()
		if request.POST.__contains__('first_name'):
			row.first_name=request.POST['first_name']
		if request.POST.__contains__('last_name'):
			row.last_name=request.POST['last_name']
		row.save()

		return HttpResponse(serializers.serialize( "json", [row] ), content_type="application/json")			# 如果不是 application/json 會變成下載
