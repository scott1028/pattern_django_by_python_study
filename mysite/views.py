# coding:utf-8

from django.http import HttpResponse
import datetime

# 直接 Response
def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# 使用 HTML Template File
from django.template.loader import get_template 		# 讀取模板
from django.template import Context						# Replace Context 用
import time

# 使用 mysite/mysite/templates/layout.html 的模板, 於 mysite/mysite/settings.py 內有設定。
def layout(request):
	now = time.time()
	t = get_template('layout.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)
