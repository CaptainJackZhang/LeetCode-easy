#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/6 12:57
@E-mail:    zhangxianlei117@gmail.com
"""
import json


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)
    # Now convert that list into linked list
    dummyRoot = Node(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = Node(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        p = head
        cur = None
        pre = None
        while p is not None:
            cur = p.next
            p.next = pre
            pre = p
            p = cur
        return pre


if __name__ == '__main__':
    s = Solution()
    h1 = Node(1)
    h2 = Node(2)
    h3 = Node(3)
    h4 = Node(4)
    h1.next = h2
    h2.next = h3
    h3.next = h4

    ret = s.reverseList(h1)
    print listNodeToString(ret)
