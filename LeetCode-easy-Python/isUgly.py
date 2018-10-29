#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/12 13:40
@E-mail:    zhangxianlei117@gmail.com
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        while (num>1):
            if (num%2==0):
                num/=2
            elif num%3==0:
                num/=3
            elif num%5==0:
                num/=5
            else:
                return False
        return True

if __name__ == '__main__':
    s= Solution()
    print s.isUgly(14)
