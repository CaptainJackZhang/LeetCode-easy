#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/20 14:06
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while (num > 0):
            num -= i
            i += 2
        return num == 0


if __name__ == '__main__':
    s = Solution()
    print s.isPerfectSquare(6)
