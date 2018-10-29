#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/26 14:21
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ji = 0
        ou = 0
        lis = {}
        for i in set(s):
            lis[i] = s.count(i)
        for i in lis:
            if lis[i] % 2 == 0: ou += lis[i]
            if lis[i] % 2 == 1:
                ji += 1
                ou += lis[i]-1
        if ji > 1:
            ji = 1
        return ou + ji


if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome('abccccddA')
