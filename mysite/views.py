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

# python object ot json
# 參考：http://stackoverflow.com/questions/9262278/django-view-returning-json-without-using-template
from django.core import serializers			# 給 model 用的
from django.utils import simplejson 		# 簡單的 Python 資料型態轉換用

def get_json(request):
	#
	some_data_to_dump = {
		'some_var_1': 'foo',
		'some_var_2': 'bar',
	}

	#
	data=simplejson.dumps(some_data_to_dump)

	#
	return HttpResponse(data, mimetype='application/json')

	#return HttpResponse(serializers.get_serializer( "xml", Foo.objects.all() ), content_type="application/json")