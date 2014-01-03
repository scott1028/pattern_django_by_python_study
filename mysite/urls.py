# coding:utf-8

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.views.home', name='home'),		# 看來格式似乎是 url({regexp pattern},{module path pattern}, name={any name you want})
    
    #
    url(r'^blog/', include('blogs.urls' )),				# 看來除了使用預設的 urls.py 的設定外個別 App 也可以有自己的獨門的 Router
    													# 代表當遇到 /blog/ 這種開頭的網址其後半段的 routes 參考 mysite/blogs/urls.py 的 routes 設定
    													# 這個部份很像 rails routes 的 collection 多層網址設定

    #
    url(r'^tt$', 'books.views.home'),					# 讓 /tt 網址導向取得 books.views.home 的方法與執行結果

    #
    url(r'^admin/', include(admin.site.urls)),			# 預設的後台
)
