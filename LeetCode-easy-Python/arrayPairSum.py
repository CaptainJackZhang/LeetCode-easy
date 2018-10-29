#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/29 11:01
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result


if __name__ == '__main__':
    s = Solution()
    print s.arrayPairSum([1, 4, 3, 2])
