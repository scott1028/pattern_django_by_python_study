# coding:utf-8

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:		           
    url(r'^abc/(?P<myParameter>\w+)', 'parametertest.views.current_datetime')	 # 看來除了使用預設的 urls.py 的設定外個別 App 也可以有自己的獨門的 Router
)