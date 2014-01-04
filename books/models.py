# coding:utf-8
# Model Field 的相關設定參考：https://docs.djangoproject.com/en/dev/ref/models/fields

from django.db import models

# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# my model
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # 可以定義你想儲存 Image 的位置
    # 注意：如果 upload_to 輸入 'images/' 會從 admin/person/:id/images/filename, 這裡設定的是絕對路徑。
    image=models.ImageField(upload_to='images/')
