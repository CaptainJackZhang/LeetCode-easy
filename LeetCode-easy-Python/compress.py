#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/29 14:39
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        com = []
        counts = 1
        for i in range(0, len(chars)-1):
            if chars[i] not in com:
                com.append(chars[i])
            else:
                counts += 1
                if chars[i] != chars[i + 1]:
                    for j in str(counts):
                        com.append(j)
                    counts = 1
        


if __name__ == '__main__':
    s = Solution()
    for i in s.compress(["a", "a", "b", "b", "b", "c", "c"]):
        print i
