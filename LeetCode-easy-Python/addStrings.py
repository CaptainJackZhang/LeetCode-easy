#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/28 08:29
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) + int(num2))


if __name__ == '__main__':
    s = Solution()
    print s.addStrings('3456743666666666666666666666663456743666666666666666666666666666666666666567866666666666665678',
                       '45678903456734567436666666666666666666666666666345674366666666666666666666666666666666666656786666666656788904567')
