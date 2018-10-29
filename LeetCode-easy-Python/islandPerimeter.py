#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/16 13:42
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        h = len(grid)
        w = len(grid[0])

        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        perimeter = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    perimeter += 4
                    # 去重
                    for d in direction:
                        x = i + d[0]
                        y = j + d[1]
                        if x >= 0 and x < h and y >= 0 and y < w and grid[x][y] == 1:
                            perimeter -= 1
        return (perimeter)

if __name__ == '__main__':
    s=Solution()
    print s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
