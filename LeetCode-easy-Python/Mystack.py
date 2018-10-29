#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/7 08:38
@E-mail:    zhangxianlei117@gmail.com
"""
from Queue import Queue


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        if self.q1.qsize() == 1:
            res = self.q1.get()
            tmp = self.q2
            self.q2 = self.q1
            self.q1 = tmp
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        if self.q1.qsize() == 1:
            res = self.q1.get()
            self.q2.put(res)
            tmp = self.q2
            self.q2 = self.q1
            self.q1 = tmp
        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not bool(self.q1.qsize() + self.q2.qsize())


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == '__main__':
    stack = MyStack()
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print stack.pop()
    print stack.top()
    print stack.pop()
    print stack.pop()
    print stack.empty()