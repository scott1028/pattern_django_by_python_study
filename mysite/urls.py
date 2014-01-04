# coding:utf-8

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.views.home', name='home'),		            # 看來格式似乎是 url({regexp pattern},{module path pattern}, name={any name you want})
    
    #
    url(r'^blog/', include('blogs.urls' )),				            # 看來除了使用預設的 urls.py 的設定外個別 App 也可以有自己的獨門的 Router
    													            # 代表當遇到 /blog/ 這種開頭的網址其後半段的 routes 參考 mysite/blogs/urls.py 的 routes 設定
    													            # 這個部份很像 rails routes 的 collection 多層網址設定

    #
    url(r'^tt$', 'books.views.home'),					            # 讓 /tt 網址導向取得 books.views.home 的方法與執行結果

    #
    url(r'^persons$', 'books.views.persons'),                      # 存取 books app 內的 persons model 資料

    #
    url(r'^layout$', 'mysite.views.layout'),                        # 採用 mysite/views.py 內的 layout Method 的 Router

    #
    url(r'^get_json$', 'mysite.views.get_json'),                    # get_json api

    #
    url(r'^get_or_post$', 'mysite.views.handle_post_and_get'),       # 處理客戶端提交資料

    #
    url(r'^admin/', include(admin.site.urls)),			            # 預設的後台
)

# 引入 setting modules
# 參考：https://docs.djangoproject.com/en/dev/ref/urls/
from django.conf import settings
from django.conf.urls.static import static

# 增加 MEDIA_URL 部分
# 與 static_url 的差異有點大, STATIC FILE 的設定在 settings.py 內就可以完成了。
#
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)