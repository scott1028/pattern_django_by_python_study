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
