# -*- coding: utf-8 -*-
'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        s = '' if self.left is None else '(%s)<='%self.left
        s += str(self.val)
        s += '' if self.right is None else '=>(%s)'%self.right
        return s
    def listStr(self):
        s = '(%s)' % (None if self.left is None else self.left.val)
        s += str(self.val)
        s += '=>%s' % (None if self.right is None else self.right.listStr())
        return s

def convert(root):
    if root is None:
        return None
    head, tail = convertCore(root)
    return head

def convertCore(root):
    head = tail = None
    if root.left is None:
        head = root
    else:
        head,root.left = convertCore(root.left)
        root.left.right = root
    if root.right is None:
        tail = root
    else:
        root.right,tail = convertCore(root.right)
        root.right.left = root
    return head, tail

'''
思路：采用后序遍历。先将左右节点变成链表，再将根节点的左右指针分别指向左链表的末尾和右链表的开头。最后返回左链表的头结点
边界：空树，只有根节点，只有左链表，只有右链表
'''
# 测试用例
print('输入：%s' % None, '输出：%s' % convert(None))
node1 = TreeNode(1)
print('输入：%s' % node1, '输出：%s' % convert(node1).listStr())
node1,node2,node3 = [TreeNode(i) for i in range(3)]
node3.left = node2
node2.left = node1
print('输入：%s' % node3, '输出：%s' % convert(node3).listStr())
node1,node2,node3 = [TreeNode(i) for i in range(3)]
node1.right = node2
node2.right = node3
print('输入：%s' % node1, '输出：%s' % convert(node1).listStr())
node1,node2,node3,node4 = [TreeNode(i) for i in range(4)]
node1.right = node3
node3.left = node2
node3.right = node4
print('输入：%s' % node1, '输出：%s' % convert(node1).listStr())
