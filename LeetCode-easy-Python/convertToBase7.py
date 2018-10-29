#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/22 08:52
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        fu = False
        if num==0:
            return "0"
        if num < 0:
            num = abs(num)
            fu = True
        while num > 0:
            ge = num % 7
            num = num / 7
            result += str(ge)
        if fu:
            return '-'+result[::-1]
        return result[::-1]


if __name__ == '__main__':
    s = Solution()
    print s.convertToBase7(0)
