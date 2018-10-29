#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/20 13:35
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2:
                    ret.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if i in nums1:
                    ret.append(i)
                    nums1.remove(i)
        return ret


if __name__ == '__main__':
    s = Solution()
    print s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
