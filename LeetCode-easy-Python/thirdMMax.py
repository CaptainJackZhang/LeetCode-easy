#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/27 13:10
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = None
        second = None
        third = None
        nums = list(set(nums))
        if len(nums) <= 2:
            return max(nums)
        for i in nums:
            if i > first:
                third = second
                second = first
                first = i
            elif i > second:
                third = second
                second = i
            elif i > third:
                third = i
        return third


if __name__ == '__main__':
    s = Solution()
    print s.thirdMax([1,2,-2147483648])
