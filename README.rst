以下逐步教學 Django 專案開發過程
================================

建立專案
--------
	django-admin.py startproject mysite


建立 Feature ( 以 books App為例 )
---------------------------------
	cd mysite
	manage.py startapp books


設定 urls.py
------------
	# 整個專案的預設讀取 urls.py 位於 startproject_name/urls.py, 即 mysite/mysite/urls.py

urls.py 範本
------------
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

