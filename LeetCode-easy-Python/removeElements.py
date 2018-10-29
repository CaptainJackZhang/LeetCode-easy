#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    Jack
@datetime:  2018/9/1 13:50
@E-mail:    zhangxianlei117@gmail.com
"""
import json


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        pre = self.head
        length = 0
        while pre:
            length += 1
            pre = pre.next
        return length

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head:
            while head.val == val:   #第一个就是要删除的
                head = head.next
                if head is None:
                    return head
            pre = Node(None)
            pre.next = head
            prep = pre
            while prep.next:
                if prep.next.val == val:
                    prep.next = prep.next.next
                else:
                    prep=prep.next
        return head


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


def stringToInt(input):
    return int(input)


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


if __name__ == '__main__':
    s = Solution()
    head = stringToListNode([1, 2, 3, 4, 5, 6, 3])
    val = stringToInt(3)
    ret = s.removeElements(head, val)
    out = listNodeToString(ret)
    print out
