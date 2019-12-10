# -*- coding: utf-8 -*-
import django
from django.conf.urls import url, include
from rest_framework_tus.views import UploadViewSet

from .routers import TusAPIRouter

app_name = 'rest_framework_tus'

router = TusAPIRouter()
router.register(r'files', UploadViewSet, base_name='upload')

if django.VERSION >= (2, 0):
    urlpatterns = [
        url(r'', include((router.urls, 'rest_framework_tus'), namespace='api'))
    ]
else:
    urlpatterns = [
        url(r'', include(router.urls, namespace='api'))
    ]
