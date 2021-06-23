# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
========================================
# @Author   : Mr_Chen
# @time     : 2021/6/22 21:34
# @File     : tasks.py
# @Notes    : 设置Celery任务，执行消息队列里的任务
=========================================
"""
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .dingtalk import send


@shared_task
def send_dingtalk_message(message, type, at):
    send(message, type, at)
