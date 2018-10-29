#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/10 12:29
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_raw = sorted(nums)
        Sum = 0
        for i in range(1, len(nums_raw)):
            Sum += (nums_raw[i] - nums_raw[0])
        return Sum


if __name__ == '__main__':
    s = Solution()
    print s.minMoves([1, 2, 3])
