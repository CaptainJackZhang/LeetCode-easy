#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    Jack
@datetime:  2018/8/31 13:47
@E-mail:    zhangxianlei117@gmail.com
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class ChainTable(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def __len__(self):
        pre = self.head
        length = 0
        while pre:
            length += 1
            pre = pre.next
        return length

    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        # 如果没有头结点（为空），则当前节点为头结点
        if not self.head:
            self.head = item
            self.length += 1
        else:
            # 如果有头节点，则找到尾节点然后将新节点追加到末尾。
            node = self.head
            while node.next:
                node = node.next
            node.next = item
            self.length += 1

    def get(self, index):
        index = index if index >= 0 else len(self) + index
        if len(self) < index or index < 0:
            return None
        pre = self.head
        while index:
            pre = pre.next
            index -= 1
        return pre

    def set(self, index, data):
        node = self.get(index)
        if node:
            node.val = data
        return node

    # 在index插入数字
    """
        1.index 插入节点位置包括正负数
        2.找到index-1-->pre_node的节点
        3.pre_node.next-->node
          node.next-->pre_node.next.next
        4.head
        :param index:
        :param data:
        :return:
    """

    def insert(self, index, data):
        node = Node(data)
        if abs(index + 1) > len(self):
            return False
        index = index if index >= 0 else len(self) + index + 1
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pre = self.get(index - 1)
            if pre:
                next = pre.next
                pre.next = node
                node.next = next
            else:
                return False

    def delete(self, index):
        if abs(index + 1) > len(self):
            return False
        pre = self.head
        index = index if index >= 0 else len(self) + index
        prep = None
        # 找到要断裂键的点
        while index:
            prep = pre  # 断裂的前一个点
            pre = pre.next  # 断裂的后一个点
            index -= 1
        if not prep:
            self.head = pre.next
        else:
            prep.next = pre.next
        return pre.val

    def clear(self):
        self.head = None


if __name__ == '__main__':
    chain = ChainTable()
    for i in [1, 3, 4, 5, 7]:
        chain.append(i)
    chain.set(2, 9)
    chain.insert(2, 11)
    print chain.get(2)
    print "You have delete:", chain.delete(2), "from list!"
    print chain.get(2)
