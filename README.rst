========================================
這是一個 CRUD 的雛型，可以用開發專案用。
========================================

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


**增加 Django Admin 後台可見的 Tables**

	::

		# app/admin.py 內增加 Model 註冊：
			from django.contrib import admin

			# Register your models here.
			from models import *

			# 定義原本的 Admin Class
			class AuthorAdmin(admin.ModelAdmin):pass

			# 增加一個 Model 進去, 之後就可以在後台看到了
			admin.site.register(Person, AuthorAdmin)


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


**Django Admin 的使用**

	::

		# 在 /admin 登入, 以 manage.py syncdb 時設定的帳號密碼登入。
		# 新增 User 後必須勾選, 可登入的選項, 之後該使用者才可以正常登入,
		  另外 Group 部分可以做使用者權限群組, 基本上很夠用了：
			[v] 工作人員狀態
				指定是否使用者可以登入此管理網站。

			[v] Staff status
				Designates whether the user can log into this admin site


**Django Staic File(JavaScript, CSS, Images 等) 相關設定**

	::

		# 參考：https://docs.djangoproject.com/en/1.6/howto/static-files/
		# settings.py 內設定 STATIC_URL(可以設定多個) 與 STATICFILES_DIRS。
		# 參考範例：
			BASE_DIR = os.path.dirname(os.path.dirname(__file__))
			...
			STATIC_URL = '/static/'
			STATICFILES_DIRS = (
			    os.path.join(BASE_DIR, 'public'),		# 可以用來存上傳檔案的路徑
			)


		# 注意與 Media File 的設定不大一樣。


**Django Media File(Upload Files, User Images 等) 相關設定**
	
	::

		# 參考：https://docs.djangoproject.com/en/dev/ref/models/fields 
			SET VS90COMNTOOLS=%VS110COMNTOOLS% for Unable to find vcvarsall.bat
		  	with Visual Studio 2012。

		# 必須先安裝 pip install pillow 與 pip install PIL 兩個套件才可以使用
			在 Model 內定義 Image Field 並設定儲存路徑。
			在 Table 內定義 image Column 並設定為文字。

		# models.py
			...
			class Person(models.Model):
				first_name = models.CharField(max_length=30)
				last_name = models.CharField(max_length=30)

				# 增加圖片欄位, 並指定實體 Media 儲存路徑。
				image=models.ImageField(upload_to='images')
			...

		# 其中 /images/ 為 Model 內的 ImageField(path_to='images') 修正。
			# settings.py	
				...
				MEDIA_URL = '/media/'
				...

			# urls.py
			# 參考：https://docs.djangoproject.com/en/dev/ref/urls/
				...
				from django.conf import settings
				from django.conf.urls.static import static

				urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
				...

		# Update Media File 跟 Delete Medai File when removing Record
			# models.py
				...
				class Person(models.Model):
				    first_name = models.CharField(max_length=30)
				    last_name = models.CharField(max_length=30)
				    
				    # 增加圖片欄位, 並指定實體 Media 儲存路徑。
				    image=models.ImageField(upload_to='media')

				    # 增加 delete 的 Trigger 當刪除紀錄的時候一併刪除圖片
				    # 即使沒設定圖片會一直存著, 但是也不會出現其他 Bug。
				    def delete(self, *args, **kwargs):
						self.image.delete(False)
						super(Person, self).delete(*args, **kwargs)

					# 如果執行 Update 的時候要替換 Image 不使用的當案
				    # 簡單來說就是 Update Image 的時候會刪除舊的 Image File
				    def save(self, *args, **kwargs):
				        # delete old file when replacing by updating the file
				        try:
				            this = Person.objects.get(id=self.id)
				            if this.image != self.image:this.image.delete(save=False)
				        except: pass # when new photo then we do nothing, normal case          
				        super(Person, self).save(*args, **kwargs)
				...


**STATIC_URL & MEDIA_URL 在 Django 框架內的原意**

	::

		# settings.py
		#
			MEDIA_URL is used to point to the base URL for user-generated content
			          such as uploaded images, files, that sort of thing.

			STATIC_URL is used as the prefix for JavaScript, CSS, etc.

		# 
		# urls.py
			**增加 MEDIA_URL 部分**
			...
			from django.conf import settings
			from django.conf.urls.static import static
			
			urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
			...


**Extend Package**

	::

		pip install django-tastypie
		# Django-tastypie - RestFul Web Service API framework for Django
		

**常用的命令**
	
	::

		Type 'manage.py help <subcommand>' for help on a specific subcommand.

		Available subcommands:

		[auth]
		    changepassword
		    createsuperuser

		[django]
		    check
		    cleanup
		    compilemessages
		    createcachetable
		    dbshell
		    diffsettings
		    dumpdata
		    flush
		    inspectdb
		    loaddata
		    makemessages
		    runfcgi
		    shell
		    sql
		    sqlall
		    sqlclear
		    sqlcustom
		    sqldropindexes
		    sqlflush
		    sqlindexes
		    sqlinitialdata
		    sqlsequencereset
		    startapp
		    startproject
		    syncdb
		    test
		    testserver
		    validate

		[sessions]
		    clearsessions

		[staticfiles]
		    collectstatic
		    findstatic
		    runserver
