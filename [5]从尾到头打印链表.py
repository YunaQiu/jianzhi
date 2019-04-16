# -*- coding: utf-8 -*-
'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "%s->%s" % (self.val,self.next)

def reverseList(listNode):
    stack = []
    node = listNode
    if node is None:
        return []
    stack.append(node.val)
    while (node.next != None):
        node = node.next
        stack.append(node.val)
    array = []
    while len(stack)>0:
        num = stack.pop()
        array.append(num)
    return array

'''
思路：要求返回的是一个数组，相当于第一次顺序读取时压入栈，第二次再从末尾读出来存入目标数组
测试用例：
输入空链表
只有一个值的链表
正常链表
'''
listNode1 = ListNode(3)
listNode2 = ListNode(2)
listNode3 = ListNode(4)
print('输入：%s, 输出：%s, 答案：%s' % (None, reverseList(None), []))
print('输入：%s, 输出：%s, 答案：%s' % (listNode1, reverseList(listNode1), [3]))
listNode1.next = listNode2
listNode2.next = listNode3
print('输入：%s, 输出：%s, 答案：%s' % (listNode1, reverseList(listNode1), [4,2,3]))
