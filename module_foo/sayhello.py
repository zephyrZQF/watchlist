# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/12/30 19:27
# @Author    : zephyr
# @File      ：sayhello.py


def sayhello(to=None):
    if to:
        return 'Hello,%s!' % to
    return 'Hello!'
