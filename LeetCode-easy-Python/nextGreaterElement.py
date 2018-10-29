#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/19 09:26
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        index = [-1] * len(findNums)
        while i < len(findNums):
            index2 = nums.index(findNums[i])
            for j in range(index2, len(nums)):
                if nums[j] > findNums[i]:
                    index[i] = nums[j]
                    break
            i+=1
        return index



if __name__ == '__main__':
    s = Solution()
    print s.nextGreaterElement(findNums=[4, 1, 2], nums=[1, 3, 4, 2])
