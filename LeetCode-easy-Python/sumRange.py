#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/17 12:27
@E-mail:    zhangxianlei117@gmail.com
"""


# class NumArray(object):
#
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums
#
#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         while (j - i) > 1:
#             mid = (i + j) / 2
#             return self.sumRange(i, mid)+self.sumRange(mid + 1, j)
#         return sum(self.nums[i:j]) + self.nums[j]

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
class NumArray(object):

    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = [0] * (len(nums)+1)
        for i in xrange(len(nums)):
            self.sums[i+1] = self.sums[i] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1] - self.sums[i]
    # 在初始化的时候，将从第一个元素开始到当前位置的所有元素的和求出来，存放到数组sums中。那么每次求一个范围的和时，只要计算两个下标处和的差即可。

if __name__ == '__main__':
    obj = NumArray(nums=[-2, 0, 3, -5, 2, -1])
    print obj.sumRange(0, 5)
