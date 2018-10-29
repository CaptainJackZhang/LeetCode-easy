#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/6 13:35
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if i - dic[nums[i]] <= k:
                    return True
                else:
                    dic[nums[i]] = i
        return False


if __name__ == '__main__':
    s = Solution()
    print s.containsNearbyDuplicate(nums=[2, 2], k=3)
