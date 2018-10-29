#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/25 14:02
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1 = list(s)
        s1.sort()
        l1 = list(t)
        l1.sort()
        i = 0
        while (i < len(s1)):
            if s1[i] != l1[i]:
                return l1[i]
            i += 1
        return l1[-1]



if __name__ == '__main__':
    s = Solution()
    print s.findTheDifference(s="abcd", t="abccd")
