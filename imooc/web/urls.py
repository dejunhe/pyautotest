# -*- coding:utf-8 -*-


from django.conf.urls import url
from django.contrib import admin

from web.views import Login

urlpatterns = [
    url(r'^index/', Login),
]
