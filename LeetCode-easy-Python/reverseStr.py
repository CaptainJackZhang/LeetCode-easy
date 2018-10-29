#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/25 14:32
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        for i in range(0, len(s), 2 * k):
            result += s[i:i+k][::-1]
            result += s[i+k:i+2*k][::]
        return result


if __name__ == '__main__':
    s = Solution()
    print s.reverseStr(s="abcdefg", k=2)
