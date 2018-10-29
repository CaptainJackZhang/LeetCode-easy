#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/20 14:19
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if ((a & b) == 0):
            return a | b
        return self.getSum(a ^ b, (a & b) << 1)


if __name__ == '__main__':
    s = Solution()
    print s.getSum(1, 2)
