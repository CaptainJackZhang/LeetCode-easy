#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/14 13:29
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.append(0)
        return nums

# class Solution(object):    优化代码
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         count = 0
#         j = 0
#         for i in range(len(nums)):
#             if(nums[i]):
#                 nums[j] = nums[i]
#                 j += 1
#             #else:
#              #   count += 1
#         for i in range(j, len(nums)):
#             nums[i] = 0
if __name__ == '__main__':
    s = Solution()
    li = s.moveZeroes([0, 1, 0, 3, 12])
    for i in li:
        print i

