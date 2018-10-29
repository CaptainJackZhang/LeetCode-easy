#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/21 14:39
@E-mail:    zhangxianlei117@gmail.com
"""
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=0
        r=n
        while(l<r):
            mid=(l+r)/2
            res=guess(mid)
            if res==-1:
                r=mid-1
            elif res==1:
                l=mid+1
            else:
                return mid


if __name__ == '__main__':
    
