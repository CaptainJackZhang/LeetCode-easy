#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/17 11:42
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        i = 0
        words = str.split()
        if len(list(pattern)) != len(list(str.split())):
            return False

        for alpha in pattern:
            if dic1.has_key(alpha):
                if dic1[alpha] != words[i]:
                    return False
            else:
                dic1[alpha] = words[i]

            if dic2.has_key(words[i]):
                if dic2[words[i]] != alpha:
                    return False
            else:
                dic2[words[i]] = alpha
            i += 1
        return True

# class Solution(object):    优化版更简洁
#     def wordPattern(self, pattern, str):
#         """
#         :type pattern: str
#         :type str: str
#         :rtype: bool
#         """
#         strlist = str.split()
#
#         if len(pattern) != len(strlist):
#             return False
#         return (len(set(pattern))) == (len(set(strlist))) == (len(set(zip(pattern, strlist))))

if __name__ == '__main__':
    s = Solution()
    print s.wordPattern(pattern="aaa", str="aa aa aa aa")
