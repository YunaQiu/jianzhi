# -*- coding: utf-8 -*-
'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
    def __str__(self):
        result = str(self.label)
        if self.random is not None:
            result += '(->%s)' % self.random.label
        return '%s->%s' % (result, self.next)
def clone(pHead):
    if pHead is None:
        return None
    old = pHead
    while old is not None:
        new = RandomListNode(old.label)
        new.next = old.next
        old.next = new
        old = new.next

    head = pHead.next
    old,new = pHead, head
    while old is not None:
        if old.random is not None:
            new.random = old.random.next
        old = new.next
        new = None if new.next is None else new.next.next

    old,new = pHead, head
    while old is not None:
        old.next = new.next
        new.next = None if new.next is None else new.next.next
        old = old.next
        new = new.next
    return head

'''
思路：遍历三遍，第一遍把每个节点复制一份，并接在旧节点的后面，形成新旧间隔串联起来的链表。第二遍把新节点的随机指针分别指向旧节点随机指针的下一个节点（即平移链接关系）。第三遍把新旧节点连接到各自的顺序节点
边界：空链表，只有一个节点，有两个节点，有三个及以上节点，随机指针指向前面，随机指针指向后面
'''
node1 = RandomListNode(1)
node2 = node1.next = RandomListNode(2)
node3 = node2.next = RandomListNode(3)
node4 = node3.next = RandomListNode(4)
print('输入：%s，输出：%s' % (None, clone(None)))
print('输入：%s，输出：%s' % (node4, clone(node4)))
print('输入：%s，输出：%s' % (node3, clone(node3)))
print('输入：%s，输出：%s' % (node2, clone(node2)))
node2.random = node4
node3.random = node1
print('输入：%s，输出：%s' % (node1, clone(node1)))
