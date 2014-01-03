# coding:utf-8

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")		# mysite/settings.py 為此 django project 的主要 configure 文件

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
