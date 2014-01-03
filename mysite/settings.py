# coding:utf-8

"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's6vxwp_9yb5_91l(%yq#7*^4)gg-gaq2&z(!s)n+2k-0d2gq@o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# 如果有自己增加 App 要從這邊設定
# 修改好之後要執行 manage.py syncdb 這個指令類似 rake db:migrate 可以將新增的 app 建立進去
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books'         # add my app which is created by " manage.py startapp books " command!, 資料庫表單的命名規則為 appName_className, 可透過 manage.py shell 管理操作 Class, 其操作方式類似 rails c
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',                      # 全域關閉 CRSF 保護
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
#
# 設定靜態資料的路由前奏
STATIC_URL = '/static/'

#
# 添加一個 TEMPALTE 的存放 PATH
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)
print os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/')

#
# 增加靜態資料的目錄(爬超久的文...真不知道該說啥 django 的文件也太難找了)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'public'),        # 可以設定多個
)
print os.path.join(BASE_DIR, 'public')

#
# 利用最上方的 BASE_DIR 來做路由基礎
print BASE_DIR