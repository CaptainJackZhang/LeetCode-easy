#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/24 16:21
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = 0
        # if len(word)==1:
        #     return True
        if word[0].isupper():
            count += 1
            for alpha in word[1:]:
                if alpha.isupper():
                    count += 1
        else:
            for alpha in word[1:]:
                if alpha.isupper():
                    return False
            return True
        return count == len(word) or count == 1


if __name__ == '__main__':
    s = Solution()
    print s.detectCapitalUse('ggg')
