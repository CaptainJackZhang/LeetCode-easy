#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/5 08:57
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)


if __name__ == '__main__':
    s = Solution()
    print s.containsDuplicate([1, 2, 3, 1])
