#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/7 09:06
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while (n > 1) and (n % 2 == 0):
            n /= 2
        return (n == 1)


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 101):
        print 'The number ', i, 'is ', s.isPowerOfTwo(i)
