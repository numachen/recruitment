# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
========================================
# @Author   : Mr_Chen
# @time     : 2021/5/31 22:29
# @File     : urls.py
# @Notes    : 职位列表URL
=========================================
"""

from django.conf.urls import url
from django.urls import path
from jobs import views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    # 职位列表
    path("joblist/", views.joblist, name="joblist"),
    # url(r"^job/(?P<job_id>\d+)/$", views.detail, name="detail")
    # 职位详细
    path("job/<int:job_id>/", views.detail, name="detail"),

    path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),
    # 查看简历原始的页面
    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),
    # 首页自动跳转到  职位列表
    url(r"^$", views.joblist, name="name"),
    # 所有报错，都上报到sentry服务器，进行错误收集，这只是一个测试视图
    path('sentry-debug/', trigger_error),
]
