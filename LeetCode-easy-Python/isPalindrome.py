#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Jack
@file: isPalindrome.py
@datetime:2018/8/30 14:05
@software: PyCharm
@E-mail: zhangxianlei117@gmail.com
"""


def isPalindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]


print isPalindrome(12345431)
