#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    Jack
@datetime:  2018/8/31 15:55
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        if n<0: return False
        elif n==1: return True
        while (n > 0):
            sum += (n % 10) ** 2
            n /= 10
        if sum ==4:
            return False
        #self.record.append(sum)
        if sum == 1:
            return True
        else:
            return self.isHappy(sum)


if __name__ == '__main__':
    s = Solution()
    num = s.isHappy(1)
    print num
