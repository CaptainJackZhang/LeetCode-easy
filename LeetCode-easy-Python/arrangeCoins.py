#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/29 14:16  ¤
@E-mail:    zhangxianlei117@gmail.com
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(((8*n+1)**0.5-1)/2)





if __name__ == '__main__':
    s=Solution()
    print s.arrangeCoins(8)
    
