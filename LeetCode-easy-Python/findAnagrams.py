#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/28 08:38
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s)!=len(p)
        c=set(p)
        for i in c:
            if s.count(i)!=p.count(i):
                return False
        return True


        return res


if __name__ == '__main__':
    s = Solution()
    print s.findAnagrams(s="cbaebabacd", p="abc")
