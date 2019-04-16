# -*- coding: utf-8 -*-
'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val)

def firstLoopNode(node):
    if node is None:
        return None
    routeList = []
    speNode = ListNode('#')
    nd = node
    while nd.next is not speNode:
        routeList.append(nd)
        if nd.next is None:
            nd = None
            break
        nextNd = nd.next
        nd.next = speNode
        nd = nextNd
    for i in range(len(routeList)):
        routeList[i].next = routeList[i+1] if i < len(routeList)-1 else nd
    return nd


'''
思路：用一个数组缓存节点路径，新建一个特殊节点，从头遍历链表，并将访问过的节点的next指针都指向特殊节点。则碰到第一个指向特殊节点的节点即为入口节点。最后根据缓存路径重新连接链表
边界：节点个数为0,1,2,3，入口节点在第1、最后一个、中间。没有入口节点
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % (None, firstLoopNode(None), None))
node1 = ListNode(1)
print('输入：%s，输出：%s，答案：%s' % ('1->null', firstLoopNode(node1), None))
node1.next = node1
print('输入：%s，输出：%s，答案：%s' % ('1->1', firstLoopNode(node1), '1'))
node1.next = node2 = ListNode(2)
print('输入：%s，输出：%s，答案：%s' % ('1->2->null', firstLoopNode(node1), None))
node2.next = node1
print('输入：%s，输出：%s，答案：%s' % ('1->2->1', firstLoopNode(node1), '1'))
node2.next = node3 = ListNode(3)
node3.next = node2
print('输入：%s，输出：%s，答案：%s' % ('1->2->3->2', firstLoopNode(node1), '2'))
node3.next = node4 = ListNode(4)
print('输入：%s，输出：%s，答案：%s' % ('1->2->3->4->null', firstLoopNode(node1), None))
node4.next = node4
print('输入：%s，输出：%s，答案：%s' % ('1->2->3->4->4', firstLoopNode(node1), '4'))
node4.next = node1
print('输入：%s，输出：%s，答案：%s' % ('1->2->3->4->1', firstLoopNode(node1), '1'))
