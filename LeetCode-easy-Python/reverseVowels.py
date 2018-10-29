#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/19 13:47
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuanyin = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
        start = 0
        lis_str=list(s)
        end = len(lis_str) - 1
        while (start <= end):
            if lis_str[start] not in yuanyin:
                start += 1
            elif lis_str[end] not in yuanyin:
                end -= 1
            else:
                tmp = lis_str[start]
                lis_str[start] = lis_str[end]
                lis_str[end] = tmp
                start+=1
                end-=1
        return ''.join(lis_str)


if __name__ == '__main__':
    s = Solution()
    print s.reverseVowels('a.')
