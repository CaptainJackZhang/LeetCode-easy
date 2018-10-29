#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/13 13:40
@E-mail:    zhangxianlei117@gmail.com
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def isBadVersion(version):
    if version >= 4:
        return False
    else:
        return True


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        tail = n
        while (head < tail):
            check = n / 2 + 1
            if (isBadVersion(check) == False) and isBadVersion(check + 1) == False:
                head = check
            if (isBadVersion(check) == True) and isBadVersion(check + 1) == False:
                return check + 1
            if (isBadVersion(check) == True) and isBadVersion(check + 1) == True:
                tail = check

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #二分查找，logn的时间复杂度
        left=0;right=n
        while(True):
            mid=(left+right)//2
            if isBadVersion(mid)==False and isBadVersion(mid+1)==True:
                return mid+1
            elif isBadVersion(mid)==False and isBadVersion(mid+1)==False:
                left=mid
            elif isBadVersion(mid)==True and isBadVersion(mid+1)==True:
                right=mid
if __name__ == '__main__':
    s = Solution()
    print s.firstBadVersion(5)
