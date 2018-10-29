#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/19 08:57
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        y = 1
        i = 0
        square = int(area ** .5)
        for i in range(square, 0, -1):
            if area % i == 0:
                y = area / i
                break
        return [i, y]


if __name__ == '__main__':
    s = Solution()
    print s.constructRectangle(1)
