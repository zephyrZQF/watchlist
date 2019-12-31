# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/12/30 19:48
# @Author    : zephyr
# @File      ：test.py

import unittest
from watchlist import app,db
from watchlist.models import Movie,User

class WatchlistTestCase(unittest.TestCase):
    def setUp(self):
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
        )

        db.create_all()
        user = User(name='Test',username='test')
        user.set_password('123')
        movie = Movie(title='Test Movie Title',year='2019')
        db.session.add_all([user,movie])
        db.session.commit()

        self.client = app.test_client()
        self.runner = app.test_cli_runner()
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_app_exist(self):
        self.assertIsNone(app)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    # 测试 404 页面
    def test_404_page(self):
        response = self.client.get('/nothing')  # 传入目标 URL

        data = response.get_data(as_text=True)
        self.assertIn('Page Not Found - 404', data)
        self.assertIn('Go Back', data)
        self.assertEqual(response.status_code, 404)  # 判断响应状态码

    # 测试主页
    def test_index_page(self):
        response = self.client.get('/')

        data = response.get_data(as_text=True)
        self.assertIn('Test\'s Watchlist', data)
        self.assertIn('Test Movie Title', data)
        self.assertEqual(response.status_code, 200)
