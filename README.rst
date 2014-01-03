以下逐步教學 Django 專案開發過程
================================

建立專案
--------
	
	::
	
		django-admin.py startproject mysite


建立 Feature ( 以 books App為例 )
---------------------------------
	
	::

		cd mysite
		manage.py startapp books


設定 urls.py
------------
	
	::

		# 整個專案的預設讀取 urls.py 位於 startproject_name/urls.py, 即 mysite/mysite/urls.py

urls.py 範本
------------

	::

		url(r'^$', 'mysite.views.home', name='home'),
		# 看來格式似乎是 url({regexp pattern},{module path pattern}, name={any name you want})
		# 代表存在 mysite/mysite/views.py 的文件裡面還有一個 def home(request) 的介面
		# views.py 自己手動建立即可！

		url(r'^blog/', include('blog.urls')),
		# 看來除了使用預設的 urls.py 的設定外個別 App 也可以有自己的獨門的 Rounter
		# 代表如果採用 /blog/* 開頭後的URL轉採用 mysite/blog/urls.py 的 routes 設定。
		# 類似 rails router 的 collection 多層設定方式。
		# 可讓 app 的 urls.py 都分別獨立描述，比較好分工。

		url(r'^admin/', include(admin.site.urls)),
		# 這是預設的後台。

新增 Model 的步驟
-----------------

	::

		# model 是放在 app 內的
		# manage.py startapp books 後會產生一個 books 的資料夾裡面會有一個 models.py 的文件
		# 在 models.py 內定義一個 Class
			#
			class Person(models.Model):
				first_name = models.CharField(max_length=30)
				last_name = models.CharField(max_length=30)

		# 然後再 settings.py 內找到：
			...
			INSTALLED_APPS = (
				'django.contrib.admin',
				'django.contrib.auth',
				'django.contrib.contenttypes',
				'django.contrib.sessions',
				'django.contrib.messages',
				'django.contrib.staticfiles',
				'books'         # 把先前使用 manage.py startapp 指令建立的 app 加入
			)
			...

		# manage.py syncdb , 透過此指令做 database migration 將資料表建立即可！

Django shell 操作 ( 類似 rails c )
-----------------------------
	
	::

		# 在專案目錄下
		# /> manage.py shell
		>> 
		>> from books.models import *
		>> row=Person(first_name='scott', last_name='blue')
		>> row.save()
		>> row.first_name='alan'
		>> row.save()

Extend Package
--------------

	::

		pip install django-tastypie
		# Django-tastypie - RestFul Web Service API framework for Django

