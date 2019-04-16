# -*- coding: utf-8 -*-
'''
输入两个链表，找出它们的第一个公共结点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return '%s->%s' % (self.val, self.next)

def findNode(pHead1, pHead2):
    if pHead1 is None or pHead2 is None:
        return None
    speNode = ListNode('spe')
    pre,node = pHead1, pHead1.next
    tempList = [pre, node]
    pre.next = speNode
    while node is not None:
        pre, node = node, node.next
        pre.next = speNode
        tempList.append(node)
    node, common = pHead2, None
    while node is not None:
        if node.next == speNode:
            common = node
            break
        node = node.next
    for i in range(len(tempList)-1):
        tempList[i].next = tempList[i+1]
    return common


'''
思路：如果可以修改链表，那么最方便的操作就是创建一个特殊节点，遍历第一个链表时将走过的节点都指向特殊节点。在遍历第二个链表时，找到的第一个指向特殊节点的节点就是公共节点。(若不许拆链表，可以记录下遍历路径，最后再组装)
边界：有空链表，没有公共节点，头结点是公共节点，尾节点是公共节点
'''
# 测试用例
node1 = ListNode(1)
print('输入：%s %s, ' % (None, node1), '输出：%s, 答案:%s' % (findNode(None, node1), None))
node2 = node1.next = ListNode(2)
node4 = ListNode(4)
print('输入：%s %s, ' % (node1, node4), '输出：%s, 答案:%s' % (findNode(node1, node4), None))
node3 = node2.next = node4.next = ListNode(3)
print('输入：%s %s, ' % (node1, node4), '输出：%s, 答案:%s' % (findNode(node1, node4), node3))
node5 = node3.next = ListNode(5)
print('输入：%s %s, ' % (node1, node3), '输出：%s, 答案:%s' % (findNode(node1, node3), node3))
