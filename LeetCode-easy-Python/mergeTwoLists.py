#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    Jack
@datetime:  2018/8/31 13:33
@E-mail:    zhangxianlei117@gmail.com
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#互相插入
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2


if __name__ == '__main__':

    head1 = ListNode(2)
    n1 = ListNode(3)
    n2 = ListNode(4)
    n3 = ListNode(9)
    head1.next = n1
    n1.next = n2
    n2.next = n3

    # 有序链表
    head2 = ListNode(3)
    m1 = ListNode(5)
    m2 = ListNode(7)
    m3 = ListNode(8)
    head2.next = m1
    m1.next = m2
    m2.next = m3

    s = Solution()
    res = s.mergeTwoLists(head1, head2)
    while res:
        print(res.val)
        res = res.next
