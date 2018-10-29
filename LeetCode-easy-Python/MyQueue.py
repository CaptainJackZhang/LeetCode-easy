#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    CaptainJack
@datetime:  2018/9/10 10:11
@E-mail:    zhangxianlei117@gmail.com
"""
import copy

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """

        if self.stack2:
            return self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        tmp1 = copy.deepcopy(self.stack1)
        tmp2 = copy.deepcopy(self.stack2)
        if not tmp1 and tmp2:
            return tmp2[-1]
        else:
            while len(tmp1) > 1:
                tmp2.append(tmp1.pop())
            return tmp1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if (not self.stack1) and (not self.stack2):
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print obj.pop()
    print obj.peek()
   # param_4 = obj.empty()
   # print param_2
   # print param_4
