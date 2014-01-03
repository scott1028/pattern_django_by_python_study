# coding:utf-8
# 這份文件在預設 router /mysite/urls.py 中被 inlcude
# 基本上直接複製預設的 urls.py 內容即可！

from django.conf.urls import patterns, include, url

# 
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^blogs$', 'blogs.views.home'),					# 讓 /blog/blogs 網址導向取得 books.views.home 的方法與執行結果
    														# 其中 /blog/* 為預設的 mysite/mysite/urls.py 內的 routes 跟目錄 pattern
)
