#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/29 11:04
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r0 = 0
        c0 = 0
        new = []
        hang = []
        if len(nums) * len(nums[0]) < r * c:
            return nums
        else:
            for row in nums:
                for j in row:
                    if c0 < c:
                        hang.append(j)
                        c0 += 1
                    if r0 < r and c0 == c:
                        new.append(hang)
                        hang = []
                        r0 += 1
                        c0 = 0
            return new


if __name__ == '__main__':
    s = Solution()
    print s.matrixReshape(nums=[[1, 2], [3, 4]], r=1, c=4)
