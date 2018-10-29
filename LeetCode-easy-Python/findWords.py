#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/10/22 08:05
@E-mail:    zhangxianlei117@gmail.com
"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        firstline = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
        secondline = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'J', 'K', 'L']
        thirdline = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
        for word in words:
            flag = True
            if word[0] in firstline:
                for alpha in word[1:]:
                    if alpha not in firstline:
                        flag = False
                        break
            elif word[0] in secondline:
                for alpha in word[1:]:
                    if alpha not in secondline:
                        flag = False
                        break
            elif word[0] in thirdline:
                for alpha in word[1:]:
                    if alpha not in thirdline:
                        flag = False
                        break
            if flag:
                result.append(word)
        return result


if __name__ == '__main__':
    s = Solution()
    print s.findWords(["Aasdfghjkl","Qwertyuiop","zZxcvbnm"])
