#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/12 11:03
@E-mail:    zhangxianlei117@gmail.com
"""


# class Solution(object):
#     def repeatedSubstringPattern(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         n = len(s)
#         for i in range(1, n / 2+1):
#             if n % i == 0:
#                 substring = s[:i]
#                 j = i
#                 while j < n and s[j:j + i] == substring:
#                     j += i
#                 if j == n:
#                     return True
#         return False
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = (s * 2)[1:-1]
        #print ss
        return s in ss


if __name__ == '__main__':
    s = Solution()
    print s.repeatedSubstringPattern("aba")
