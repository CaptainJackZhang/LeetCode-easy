#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/11 13:32
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for alpha in s:
            if dict.has_key(alpha):
                dict[alpha] += 1
            else:
                dict[alpha] = 1
        for alpha in t:
            if dict.has_key(alpha):
                dict[alpha] -= 1
            else:
                return False
        for i in dict.values():
            if i != 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.isAnagram(s = "rat", t = "car")
