"""
WSGI config for function_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

#記載内容のバックアップです！問題や不具合がある場合下記の記載内容に戻りましょう！
# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "function_project.settings")

# application = get_wsgi_application()

import os
import sys

# Djangoプロジェクトのディレクトリを指定します
# path = '/home/uchiyamatakuro/Portfolio-submission3/Portfolio-submission/online_counseling_platform_submission/function_project'
# if path not in sys.path:
#     sys.path.append(path)

settings_path = '/home/uchiyamatakuro/Portfolio-submission3/Portfolio-submission/online_counseling_platform_submission/function_project'
sys.path.insert(0, settings_path)

# Djangoの設定ファイルを指定します
os.environ['DJANGO_SETTINGS_MODULE'] = 'function_project.settings'

# # Djangoの設定ファイルを指定します
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "function_project.settings")

# # Cloudinaryの環境変数を設定
# os.environ["SECRET_KEY"] = "uxavdn8ARiCFCCluRFYB7zXTu0Q"
os.environ["CLOUDINARY_URL"] = "cloudinary://849992194399532:uxavdn8ARiCFCCluRFYB7zXTu0Q@dfo6zpzik"

# WSGIアプリケーションを取得します
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
