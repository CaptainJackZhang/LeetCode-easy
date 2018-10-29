#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/26 14:05
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        arr=""
        while(i<=n):
            arr+=str(i)
            i+=1
            if len(arr)>n:
                return int(arr[n-1])
        return int(arr[n - 1])





if __name__ == '__main__':
    s=Solution()
    print s.findNthDigit(100000000)
    
