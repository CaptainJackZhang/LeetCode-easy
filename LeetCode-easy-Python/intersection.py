#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/19 14:03
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))


if __name__ == '__main__':
    s=Solution()
    print s.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
    
