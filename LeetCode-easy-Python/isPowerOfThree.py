#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/18 11:09
@E-mail:    zhangxianlei117@gmail.com
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        while(n>1):
            if n %4 !=0:
                return False
            n/=4
        return True

if __name__ == '__main__':
    s=Solution()
    print s.isPowerOfThree(5)
    
