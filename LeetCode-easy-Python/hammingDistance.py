#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/15 14:41
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        c = x ^ y
        counts = 0
        bin_num = bin(c)
        for i in bin_num[2:]:
            if i == '1':
                counts += 1
        return counts


if __name__ == '__main__':
    s = Solution()
    print s.hammingDistance(1, 4)
