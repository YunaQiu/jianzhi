# -*- coding: utf-8 -*-
'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
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

def isBalancedTree(tree):
    return True if balacedTreeDepth(tree) >= 0 else False

def balacedTreeDepth(tree):
    if tree is None:
        return 0
    leftDepth = 0 if tree.left is None else balacedTreeDepth(tree.left)
    rightDepth = 0 if tree.right is None else balacedTreeDepth(tree.right)
    if abs(leftDepth - rightDepth) <= 1:
        return max(leftDepth, rightDepth) + 1
    else:
        return -2

'''
思路：采用递归遍历。判断左右子树是否平衡树并求出深度，若深度差值不超过1，则该节点为根节点的子树是平衡树
边界：树为空，只有根节点，只有左子树，只有右子树，左右相差为1，满树
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % (None, isBalancedTree(None), True))
node1 = TreeNode(1)
print('输入：%s，输出：%s，答案：%s' % (node1, isBalancedTree(node1), True))
node2 = node1.left = TreeNode(2)
print('输入：%s，输出：%s，答案：%s' % (node1, isBalancedTree(node1), True))
node3 = node2.left = TreeNode(3)
print('输入：%s，输出：%s，答案：%s' % (node1, isBalancedTree(node1), False))
node1.right = node2
node1.left = None
print('输入：%s，输出：%s，答案：%s' % (node1, isBalancedTree(node1), False))
node4 = node1.left = TreeNode(4)
print('输入：%s，输出：%s，答案：%s' % (node1, isBalancedTree(node1), True))
node5 = node2.right = TreeNode(5)
print('输入：%s，输出：%s，答案：%s' % (node1, isBalancedTree(node1), True))
node6 = node4.left = TreeNode(6)
node7 = node4.right = TreeNode(7)
print('输入：%s，输出：%s，答案：%s' % (node1, isBalancedTree(node1), True))
