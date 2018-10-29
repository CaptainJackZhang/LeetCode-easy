#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/11 12:56
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int] 胃口
        :type s: List[int] 饼干大小
        :rtype: int
        """
        g.sort()
        s.sort()
        result = 0

        for i in s:
            if i >= g[0]:
                result += 1
                g.pop(0)
            if len(g) == 0:
                break
        return result
        # else:
        #     for i in g:
        #         if i <= s[j]:
        #             result += 1
        #             s.pop(j)



if __name__ == '__main__':
    s = Solution()
    print s.findContentChildren([1, 2, 3], [1, 1])
