#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    Jack
@datetime:  2018/8/30 14:07
@E-mail:    zhangxianlei117@gmail.com
"""


def reverse(x):
    if x >= 0:
        x = int(str(x)[::-1])
        return x if x < pow(2, 31) else 0
    else:
        x = -int(str(x)[1:][::-1])
        return x if x >= (-1) * pow(2, 31) else 0


if __name__ == '__main__':
    print reverse(120)
