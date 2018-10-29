#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/13 13:26
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (int(len(nums) * (len(nums) + 1) / 2) - sum(nums))


if __name__ == '__main__':
    s = Solution()
    print s.missingNumber([0, 1])
