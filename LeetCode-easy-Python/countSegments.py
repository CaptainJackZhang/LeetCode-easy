#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/28 08:32
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())


if __name__ == '__main__':
    s = Solution()
    print s.countSegments("Hello, my name is John")
