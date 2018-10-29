#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    Jack
@datetime:  2018/8/31 15:35
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        this_num = None
        for num in nums:
            if num != this_num:
                nums[pos] = num
                this_num = num
                pos += 1
        return pos


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    len = sol.removeDuplicates(nums)
    for i in range(0, len):
        print nums[i]
