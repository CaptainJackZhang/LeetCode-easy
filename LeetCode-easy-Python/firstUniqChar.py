#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/25 13:45
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for alpha in s:
            if dic.has_key(alpha):
                dic[alpha] += 1
            else:
                dic[alpha] = 1
        for i in s:
            if dic[i] == 1:
                return s.find(i)
        return -1


if __name__ == '__main__':
    s = Solution()
    print s.firstUniqChar('loveleetcode')
