#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/26 09:57
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = 0
        late = 0
        for alpha in s:
            if alpha == 'A':
                absent += 1
            if alpha == 'L':
                late += 1
            else:
                late = 0
            if absent > 1 or late > 2:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.checkRecord("PPALLP")
