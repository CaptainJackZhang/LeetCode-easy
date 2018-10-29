#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/12 13:17
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        for i in str(num):
            res+=int(i)
        if res>=10:
            return self.addDigits(res)
        else:
            return res




if __name__ == '__main__':
    s=Solution()
    print s.addDigits(19)
