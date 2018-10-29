#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/17 14:12
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num


if __name__ == '__main__':
    s = Solution()
    print s.findComplement(5)
