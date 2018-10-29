#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    Jack
@datetime:  2018/8/30 14:15
@E-mail:    zhangxianlei117@gmail.com
"""


def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for item in strs[1:]:
        while item.find(prefix) != 0:
            prefix = prefix[:len(prefix) - 1]
            if prefix == "":
                return ""
    return prefix


if __name__ == '__main__':
    print longestCommonPrefix(["flower", "flow", "flight"])

# 一开始比较flower,然后没有的话比较flowe,
# 再比较flow,再flo,再fl,找到公共前缀后就返回
