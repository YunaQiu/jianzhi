# -*- coding: utf-8 -*-
'''
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        strX = "" if self.left is None else "(%s)<=" % self.left
        strX += str(self.val)
        strX += "" if self.right is None else "=>(%s)" % self.right
        return strX

def treeDepth(tree):
    if tree is None:
        return 0
    leftDepth = 0 if tree.left is None else treeDepth(tree.left)
    rightDepth = 0 if tree.right is None else treeDepth(tree.right)
    depth = max(leftDepth, rightDepth)
    return depth + 1

'''
思路：采用递归遍历。求出左右两个子树的深度，取较大值加1，即为以该节点为根节点的树的深度。
边界：树为空，只有根节点，只有左子树，只有右子树，左右不平衡
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % (None, treeDepth(None), 0))
node1 = TreeNode(1)
print('输入：%s，输出：%s，答案：%s' % (node1, treeDepth(node1), 1))
node2 = node1.left = TreeNode(2)
node3 = node2.left = TreeNode(3)
print('输入：%s，输出：%s，答案：%s' % (node1, treeDepth(node1), 3))
node1.right = node2
node1.left = None
print('输入：%s，输出：%s，答案：%s' % (node1, treeDepth(node1), 3))
node4 = node1.left = TreeNode(4)
print('输入：%s，输出：%s，答案：%s' % (node1, treeDepth(node1), 3))
node5 = node2.right = TreeNode(5)
print('输入：%s，输出：%s，答案：%s' % (node1, treeDepth(node1), 3))
