#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/9 15:23
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 用一个字典, 记录下与某点相同距离的次数
        d = {}
        res = 0
        # 以每一个点为中心, 进行尝试, 看看有没有距离相同的点出现, 如果放在map中, 然后对map进行统计操作,
        # 在进行下一个点的时候 要将之前的map清空
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                d[dis] = d.get(dis, 0) + 1
            for item in d.values():
                if item >= 2:
                    res += item * (item - 1)
            d.clear()
        return res


if __name__ == '__main__':
    sol = Solution()
    points = [[0, 0], [1, 0], [2, 0]]
    res = sol.numberOfBoomerangs(points)
    print(res)


