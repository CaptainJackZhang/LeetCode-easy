#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/22 15:29
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rank = nums[:]
        rank.sort(reverse=True)
        result = [0] * len(nums)
        for i in range(len(nums)):
            place = rank.index(nums[i])
            if place == 0:
                result[i] = "Gold Medal"
            elif place == 1:
                result[i] = "Silver Medal"
            elif place == 2:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(place + 1)
        return result


if __name__ == '__main__':
    s = Solution()
    print s.findRelativeRanks([5, 4, 3, 2, 1])
