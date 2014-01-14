# coding: utf-8

from django.db import models

# Create your models here.
# my model
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Article(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Person,db_column='user_id') # 可以透過 db_column 客製化關聯欄位
    # 這行會幫 Person 增加 article_set 屬性, Article 增加 author 屬性
