import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def current_datetime(request, myParameter):
    now = datetime.datetime.now()
    html = "<html><body>It is now1 %s.</br> %s </body></html>" % (now, myParameter)
    return HttpResponse(html)