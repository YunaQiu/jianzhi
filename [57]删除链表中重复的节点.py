# -*- coding: utf-8 -*-
'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next
    def __str__(self):
        return '%s->%s' % (self.val, self.next)

def deleteRepeatNodes(headNode):
    if headNode is None:
        return None
    headP = None
    prevP, thisP = None, headNode
    while thisP is not None:
        nextP = thisP.next
        if nextP is None or thisP.val != nextP.val:
            headP = thisP if headP is None else headP
            prevP, thisP = thisP, nextP
            continue
        while nextP is not None and nextP.val == thisP.val:
            nextP = nextP.next
        thisP = nextP
        if prevP is not None:
            prevP.next = thisP
    return headP

'''
思路：准备三个指针，一个指针指向上一个结点，一个指针指向当前结点，一个指针向前查找第一个与当前结点值不同的结点。从头到尾遍历
边界：空链表，只有1个节点，2个节点且重复，2个节点不重复，3个节点，尾部节点多个重复，头部节点多个重复，中间重复
'''
# 测试用例
print('输入：%s' % None, '输出：%s，答案：%s' % (deleteRepeatNodes(None), None))
node1 = ListNode(1)
print('输入：%s' % node1, '输出：%s，答案：%s' % (deleteRepeatNodes(node1), '1->None'))
node2 = node1.next = ListNode(1)
print('输入：%s' % node1, '输出：%s，答案：%s' % (deleteRepeatNodes(node1), 'None'))
node2.val = 2
print('输入：%s' % node1, '输出：%s，答案：%s' % (deleteRepeatNodes(node1), '1->2->None'))
node2.val = 1
node3 = node2.next = ListNode(3)
print('输入：%s' % node1, '输出：%s，答案：%s' % (deleteRepeatNodes(node1), '3->None'))
node0 = ListNode(0, node1)
node4 = node2.next = ListNode(1, node3)
print('输入：%s' % node0, '输出：%s，答案：%s' % (deleteRepeatNodes(node0), '0->3->None'))
node5 = node3.next = ListNode(3)
node6 = node5.next = ListNode(3)
print('输入：%s' % node0, '输出：%s，答案：%s' % (deleteRepeatNodes(node0), '0->None'))
node7 = node0.next = ListNode(0, node3)
print('输入：%s' % node0, '输出：%s，答案：%s' % (deleteRepeatNodes(node0), 'None'))
