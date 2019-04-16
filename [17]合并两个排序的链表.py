# -*- coding: utf-8 -*-
'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "%s->%s" % (self.val,self.next)
def mergeList(pHead1, pHead2):
    if pHead1 is None:
        return pHead2
    if pHead2 is None:
        return pHead1
    head = tail = None
    if pHead1.val <= pHead2.val:
        head = tail = pHead1
        pHead1 = pHead1.next
    else:
        head = tail = pHead2
        pHead2 = pHead2.next
    while pHead1 is not None and pHead2 is not None:
        if pHead1.val <= pHead2.val:
            tail.next = pHead1
            tail = pHead1
            pHead1 = pHead1.next
        else:
            tail.next = pHead2
            tail = pHead2
            pHead2 = pHead2.next
    if pHead1 is not None:
        tail.next = pHead1
    if pHead2 is not None:
        tail.next = pHead2
    return head

'''
思路：由于要返回链接后的链表头结点，需要四个指针。一个指针固定为合成后链表的头结点head，一个指针默认指向新链表的尾节点tail，剩余两个指针p1/p2分别用于对比原链表下一节点。将新尾节点的next指向p1/p2中的较小值，然后p指针顺延下一个节点。直到其中一个链表遍历到末尾，则tail节点链接到另一链表的剩余节点上
边界：输入两个空链表，一个空链表，两个只有一个头结点的链表，两个链表正好顺序连接
'''
# 测试用例
node1 = ListNode(1)
node2 = node1.next = ListNode(2)
node3 = ListNode(3)
node4 = node3.next = ListNode(3)
node5 = ListNode(5)
print('输入：%s，%s' % (None, None), '输出：%s' % mergeList(None, None))
print('输入：%s，%s' % (node1, None), '输出：%s' % mergeList(node1, None))
print('输入：%s，%s' % (node2, node5), '输出：%s' % mergeList(node2, node5))
print('输入：%s，%s' % (node1, node3), '输出：%s' % mergeList(node1, node3))
