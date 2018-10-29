#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/9 15:43
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        if len(nums) == 0:
            return []
        nums.sort()
        cur = nums[0]
        # 左边
        if cur > 1:
            for i in range(1, cur):
                result.append(i)
        boundary = max(nums[-1], len(nums))

        i = 1

        # 中间
        while (i < len(nums)):
            if nums[i] - cur > 1:
                for j in range(cur + 1, nums[i]):
                    result.append(j)
            cur = nums[i]
            i += 1
        # 右边
        if nums[-1] < len(nums):
            for i in range(nums[-1] + 1, len(nums) + 1):
                result.append(i)
        return result


if __name__ == '__main__':
    s = Solution()
    print s.findDisappearedNumbers([1, 1])
