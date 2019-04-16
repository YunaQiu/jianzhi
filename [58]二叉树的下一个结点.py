# -*- coding: utf-8 -*-
'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
class TreeNode:
    def __init__(self, x, parent = None):
        self.val = x
        self.left = None
        self.right = None
        self.parent = parent
    def __str__(self):
        result = "" if self.left is None else "(%s)<=" % self.left
        result += str(self.val)
        result += "" if self.right is None else "=>(%s)" % self.right
        return result

def nextNode(treeNode):
    if treeNode is None:
        return None
    if treeNode.right is not None:
        treeNode = treeNode.right
        while treeNode.left is not None:
            treeNode = treeNode.left
        return treeNode
    while treeNode.parent is not None:
        if treeNode is treeNode.parent.left:
            return treeNode.parent
        treeNode = treeNode.parent
    return None

'''
思路：若该结点有右节点，则右子树的最左结点为下一个结点。若该结点没有右节点，则向上回溯，若其为父节点的左节点，则父节点为下一个结点。否则继续向上回溯，直到找到第一个为左节点的父节点，或None。
边界：空结点，只有根节点，结点没有右子树，结点有右子树，结点位于左枝，结点位于右枝，结点是最后一个中序遍历结点
'''
# 测试用例
print('树：%s，输入：%s' % (None, None), '输出：%s，答案：%s' % (nextNode( None), None))
node1 = TreeNode(1)
print('树：%s，输入：%s' % (node1, None), '输出：%s，答案：%s' % (nextNode(None), None))
print('树：%s，输入：%s' % (node1, node1.val), '输出：%s，答案：%s' % (nextNode(node1), None))
node2 = node1.right = TreeNode(2, node1)
print('树：%s，输入：%s' % (node1, node1.val), '输出：%s，答案：%s' % (nextNode(node1).val, '2'))
print('树：%s，输入：%s' % (node1, node2.val), '输出：%s，答案：%s' % (nextNode(node2), None))
node3 = node2.left = TreeNode(3, node2)
print('树：%s，输入：%s' % (node1, node2.val), '输出：%s，答案：%s' % (nextNode(node2), None))
print('树：%s，输入：%s' % (node1, node3.val), '输出：%s，答案：%s' % (nextNode(node3).val, '2'))
node4 = node3.right = TreeNode(4, node3)
print('树：%s，输入：%s' % (node1, node4.val), '输出：%s，答案：%s' % (nextNode(node4).val, '2'))
node5 = node4.right = TreeNode(5, node4)
print('树：%s，输入：%s' % (node1, node5.val), '输出：%s，答案：%s' % (nextNode(node5).val, '2'))
print('树：%s，输入：%s' % (node1, node1.val), '输出：%s，答案：%s' % (nextNode(node1).val, '3'))
