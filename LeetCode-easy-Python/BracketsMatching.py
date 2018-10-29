#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    Jack
@datetime:  2018/8/31 13:32
@E-mail:    zhangxianlei117@gmail.com
"""


def isValid(s):
    stack = []
    for ss in s:
        if ss in '([{':
            stack.append(ss)
        if ss in ')]}':
            if len(stack) <= 0:
                return False
            else:
                compare = stack.pop()
                if (compare == '(' and ss != ')') or (compare == '[' and ss != ']') or (compare == '{' and ss != '}'):
                    return False
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print isValid("{[]}")
