#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/18 11:17
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]



if __name__ == '__main__':
    s=Solution()
    print s.reverseString('A man, a plan, a canal: Panama')
