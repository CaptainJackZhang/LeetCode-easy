#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/4 10:25
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    # def isIsomorphic(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     strdict = {}
    #     cur = 0
    #     while (cur < len(s)):
    #         if strdict.get(t[cur]) == None and strdict.has_key(s[cur]) == False:
    #             strdict[t[cur]] = s[cur]
    #         if strdict.get(t[cur]) == s[cur]:
    #             cur += 1
    #         else:
    #             return False
    #     return True
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        test1 = len(set(s))
        test2 = len(set(t))
        test3 = len(set(zip(s, t)))
        return test1==test2==test3


if __name__ == '__main__':
    s = Solution()
    print s.isIsomorphic('aba', 'aaa')
