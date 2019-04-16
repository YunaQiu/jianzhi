# -*- coding: utf-8 -*-
'''
输入一个链表，反转链表后，输出新链表的表头。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "%s->%s" % (self.val,self.next)

def reverseList(head):
    if head is None:
        return None
    if head.next is None:
        return head
    pre,node = head, head.next
    pre.next = None
    next = node.next
    while node is not None:
        node.next = pre
        if next is None:
            return node
        pre = node
        node = next
        next = next.next

'''
思路：该题是要求反转旧链表，并非新建。由于顺序反转的过程中，中间会出现断链的情况，因此需要三个指针
边界：空链表，只有一个结点，有2个结点，有3个结点，有更多结点
'''
# 测试用例
node1 = ListNode(1)
node1.next = node2 = ListNode(2)
node2.next = node3 = ListNode(3)
node3.next = node4 = ListNode(4)
# print('链表：%s' % node1)
print('输入：%s，' % node1, '输出：%s，答案：%s' % (reverseList(node1), '4->3->2->1->None'))
print('输入：%s，' % node3, '输出：%s，答案：%s' % (reverseList(node3), '1->2->3->None'))
print('输入：%s，' % node2, '输出：%s，答案：%s' % (reverseList(node2), '3->2->None'))
print('输入：%s，' % node2, '输出：%s，答案：%s' % (reverseList(node2), '2->None'))
print('输入：%s，输出：%s，答案：%s' % (None, reverseList(None), None))
