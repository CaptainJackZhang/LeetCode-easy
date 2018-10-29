#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/14 13:53
@E-mail:    zhangxianlei117@gmail.com
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%4==0: return False
        else:
            return True
if __name__ == '__main__':
    
