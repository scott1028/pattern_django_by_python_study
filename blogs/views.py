# coding:utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # 這個是可以讓文字直接輸出的方法

def home(requres):
	return HttpResponse('hello world by mysite.books.views.home')