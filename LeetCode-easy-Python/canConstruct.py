#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/21 14:45
@E-mail:    zhangxianlei117@gmail.com
"""


# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         li = list(ransomNote)
#         ma = list(magazine)
#         i = 0
#         for alpha in li:
#             if alpha in ma:
#                 ma.remove(alpha)
#                 i += 1
#         return i == len(ransomNote)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        x=set(i for i in ransomNote)
        dic={}
        for i in x:
            dic[i]=ransomNote.count(i)
        for k,v in dic.items():
            if magazine.count(k)<v:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.canConstruct("aa", "aab")
