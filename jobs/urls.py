# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
========================================
# @Author   : Mr_Chen
# @time     : 2021/5/31 22:29
# @File     : urls.py
# @Notes    :
=========================================
"""

from django.conf.urls import url
from django.urls import path
from jobs import views


urlpatterns = [
    # 职位列表
    path("joblist/", views.joblist, name="joblist"),
    # url(r"^job/(?P<job_id>\d+)/$", views.detail, name="detail")
    path("job/<int:job_id>/", views.detail, name="detail"),
    # 首页自动跳转到  职位列表
    url(r"^$", views.joblist, name="name"),
]