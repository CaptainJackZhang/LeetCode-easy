#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/16 14:58
@E-mail:    zhangxianlei117@gmail.com
"""

lis = [1, 2, 3, 4]
res = []

def fuc(num):
    for i in num:
        for j in num:
            for k in num:
                if i != j and i != k and j != k:
                    a = i * 100 + j * 10 + k
                    res.append(a)
    return res

result = fuc(lis)
print (result)
