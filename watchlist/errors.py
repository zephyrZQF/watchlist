# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2020/1/1 8:34
# @Author    : zephyr
# @File      ：errors.py
from flask import render_template
from watchlist import app

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404