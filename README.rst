============================
逐步教學 Django 專案開發過程
============================

**建立專案**
	
	::
	
		django-admin.py startproject mysite


**建立 Feature ( 以 books App 為例 )**
	
	::

		cd mysite
		manage.py startapp books


**設定 urls.py**
	
	::

		# 整個專案的預設讀取 urls.py 位於 startproject_name/urls.py, 即 mysite/mysite/urls.py

**urls.py 範本**

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

**新增 Model 的步驟**

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

**過濾 views.py 的 POST 或是 GET 方法(預設只能 GET)**

	::

		1.在 views.py 內引入 "from django.views.decorators.http import require_http_methods",
		  並使用 @require_http_methods(["GET", "POST"]) 來修飾 view 的方法。
		
		@csrf_exempt
		@require_http_methods(["GET", "POST"])
		def persons(request):
			...
			return ...


**關閉 CRSF 與 Ajax Create Record 方法**

	::

		1.在 settings.py 遮蔽 'django.middleware.csrf.CsrfViewMiddleware',可以全域關閉 CRSF。
		2.在 views.py 內引入 "from django.views.decorators.csrf import csrf_exempt,csrf_protect",
		  在使用 @crsf_exempt 修飾該方法可以單獨豁免 CSRF 保護。

		@csrf_exempt
		@require_http_methods(["GET", "POST"])
		def persons(request):
			...
			return ...

**Django 專案的主要設定文件(可自行修改)**

	::

		1.manage.py 內有提到：
			#!/usr/bin/env python
			import os
			import sys

			if __name__ == "__main__":
				# mysite/settings.py 為此 django project 的主要 configure 文件
			    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

			    #
			    from django.core.management import execute_from_command_line
			    execute_from_command_line(sys.argv)

**Django shell 操作 ( 類似 rails c )**
	
	::

		# 在專案目錄下
		# /> manage.py shell
		>> 
		>> from books.models import *
		>> row=Person(first_name='scott', last_name='blue')
		>> row.save()
		>> row.first_name='alan'
		>> row.save()

**Extend Package**

	::

		pip install django-tastypie
		# Django-tastypie - RestFul Web Service API framework for Django

