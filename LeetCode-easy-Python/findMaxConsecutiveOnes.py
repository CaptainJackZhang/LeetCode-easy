#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/18 13:13
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        strnum = "".join(str(i) for i in nums)
        result = str(strnum).split('0')
        for zichuan in result:
            if len(zichuan) > max:
                max = len(zichuan)
        return max


if __name__ == '__main__':
    s = Solution()
    print s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
