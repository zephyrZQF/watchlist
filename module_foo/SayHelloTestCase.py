# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/12/30 19:28
# @Author    : zephyr
# @File      ：SayHelloTestCase.py
import unittest
from module_foo.sayhello import sayhello

class SayHelloTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sayhello(self):
        rv = sayhello()
        self.assertEqual(rv,'Hello!')

    def test_sayhello_to_somebody(self):
        rv = sayhello(to='Grey')
        self.assertEqual(rv,'Hello,Grey!')

if __name__ == '__main__':
    unittest.main()