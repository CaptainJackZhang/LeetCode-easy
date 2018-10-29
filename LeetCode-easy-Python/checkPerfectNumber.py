#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/24 16:09
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=1:
            return False
        element = 2
        perfectnum = 1
        while element <= (num ** 0.5):
            if num % element == 0:
                shang = num / element
                if shang == element:
                    perfectnum += shang
                else:
                    perfectnum += shang + element
            element += 1
        return perfectnum==num


if __name__ == '__main__':
    s = Solution()
    print s.checkPerfectNumber(1)
