#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/26 10:44
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=[]
        wordlist=s.split()
        for word in wordlist:
            result.append(word[::-1]+' ')
        return ''.join(result)[:-1:]



if __name__ == '__main__':
    s=Solution()
    print s.reverseWords( "Let's take LeetCode contest")
