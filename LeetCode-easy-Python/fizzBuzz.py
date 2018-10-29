#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/27 13:05
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lis = []
        i=1
        while(i<=n):
            if i % 15 == 0:
                lis.append('FizzBuzz')
            elif i % 5 == 0:
                lis.append('Buzz')
            elif i % 3 == 0:
                lis.append('Fizz')
            else:
                lis.append(str(i))
            i += 1
        return lis


if __name__ == '__main__':
    s = Solution()
    print s.fizzBuzz(1)
