#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    Jack
@datetime:  2018/9/3 11:06
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        countnum = 0
        flag = [True] * (n - 1)
        flag[0] = False
        for cur in range(2, n):
            if flag[cur - 1] == False:
                continue
            i = cur * 2
            while (i < n):
                if flag[i - 1]:
                    flag[i - 1] = False
                i += cur
        for i in range(1, n):
            if flag[i - 1]:
                countnum += 1
        return countnum
#大神的代码
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        numbers = [True] * (n / 2)    #只检查到根号n的情况
        for m in xrange(3, int(n ** .5) + 1, 2):  #每次都只检查奇数,因为偶数除了2都不是素数
            if numbers[m / 2]:
                numbers[m * m / 2::m] = [False] * len(numbers[m * m / 2::m])
        return sum(numbers)


if __name__ == '__main__':
    s = Solution()
    print s.countPrimes(10)
