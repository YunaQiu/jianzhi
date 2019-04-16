# -*- coding:utf-8 -*-
'''
输入一个链表，输出该链表中倒数第k个结点。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val) if self.next is None else '%s->%s'%(self.val, self.next)

def findLastKthNode(head, k):
    if k<=0 or head is None:
        return None
    n1,n2,i = head, head, 0
    while i<k:
        if n2 is None:
            return None
        n2 = n2.next
        i += 1
    while n2 is not None:
        n1 = n1.next
        n2 = n2.next
    return n1

'''
思路：定义两个指针，一个指针先走k步（若期间碰到None，则返回None），然后再两个指针一起走。当前面的指针走到尾指针时，后面的指针指向的就是倒数第K个节点
边界：空链表，只有一个节点的链表，有k-1个节点的链表，有k个节点的，有k+1个节点的，更长的
k小于等于0，k等于1，k大于1
'''
# 测试用例
node1 = ListNode(1)
node1.next = node2 = ListNode(2)
node2.next = node3 = ListNode(3)
node3.next = node4 = ListNode(4)
node4.next = node5 = ListNode(5)
node5.next = node6 = ListNode(6)
print('输入：%s %s，输出：%s，答案：%s' % (None,4, findLastKthNode(None,4), None))
print('输入：%s %s，输出：%s，答案：%s' % (node6,0, findLastKthNode(node6,0), None))
print('输入：%s %s，输出：%s，答案：%s' % (node6,1, findLastKthNode(node6,1), node6))
print('输入：%s %s，输出：%s，答案：%s' % (node6,2, findLastKthNode(node6,2), None))
print('输入：%s %s，输出：%s，答案：%s' % (node3,3, findLastKthNode(node3,3), node4))
print('输入：%s %s，输出：%s，答案：%s' % (node3,4, findLastKthNode(node3,4), node3))
print('输入：%s %s，输出：%s，答案：%s' % (node3,5, findLastKthNode(node3,5), None))
print('输入：%s %s，输出：%s，答案：%s' % (node1,4, findLastKthNode(node1,4), node3))
