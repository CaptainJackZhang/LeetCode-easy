#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Jack
@file: Twosum.py
@time: 2018/08/{DAY}
"""


def twoSum(nums, target):
    for i in range(0, len(nums) - 1):
        tmp = target - nums[i]
        for j in range(i + 1, len(nums)):
            if tmp == nums[j]:
                return [i, j]


print twoSum(nums=[2, 7, 11, 15], target=9)
