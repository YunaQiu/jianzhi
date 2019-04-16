# -*- coding: utf-8 -*-
'''
给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        result = "" if self.left is None else "(%s)<=" % self.left
        result += str(self.val)
        result += "" if self.right is None else "=>(%s)" % self.right
        return result

def getKthNode(tree, k):
    if tree is None or k < 1:
        return None
    res = findCore(tree, k)
    return res if isinstance(res, TreeNode) else None

def findCore(tree, k):
    left = findCore(tree.left, k) if tree.left is not None else 0
    if isinstance(left, TreeNode):
        return left
    if left == k-1:
        return tree
    right = findCore(tree.right, k-left-1) if tree.right is not None else 0
    if isinstance(right, TreeNode):
        return right
    return left + right + 1

'''
思路：先从左子树找第k个节点，找不到则返回树的节点个数l。l=k-1，那么根节点即为第k个。否则去右子树找第k-l-1个节点。若整个树节点少于k个，则返回None
边界：空树，k小于1，树节点比k少。目标节点在左子树第一个/最后一个，目标节点在根节点，目标节点在右子树第一个/最后一个
'''
# 测试用例
print('输入：%s %s，输出：%s，答案：%s' % (None, 2, getKthNode(None, 2), None))
node1 = TreeNode(5)
print('输入：%s %s，输出：%s，答案：%s' % (node1, 0, getKthNode(node1, 0), None))
print('输入：%s %s，输出：%s，答案：%s' % (node1, 1, getKthNode(node1, 1).val, 5))
print('输入：%s %s，输出：%s，答案：%s' % (node1, 2, getKthNode(node1, 2), None))
node2 = node1.left = TreeNode(3)
print('输入：%s %s，输出：%s，答案：%s' % (node1, 1, getKthNode(node1, 1).val, 3))
print('输入：%s %s，输出：%s，答案：%s' % (node1, 2, getKthNode(node1, 2).val, 5))
node3 = node1.right = TreeNode(8)
print('输入：%s %s，输出：%s，答案：%s' % (node1, 3, getKthNode(node1, 3).val, 8))
node4 = node2.left = TreeNode(1)
node5 = node2.right = TreeNode(4)
print('输入：%s %s，输出：%s，答案：%s' % (node1, 1, getKthNode(node1, 1).val, 1))
print('输入：%s %s，输出：%s，答案：%s' % (node1, 3, getKthNode(node1, 3).val, 4))
node6 = node3.left = TreeNode(7)
print('输入：%s %s，输出：%s，答案：%s' % (node1, 4, getKthNode(node1, 4).val, 5))
print('输入：%s %s，输出：%s，答案：%s' % (node1, 5, getKthNode(node1, 5).val, 7))
print('输入：%s %s，输出：%s，答案：%s' % (node1, 6, getKthNode(node1, 6).val, 8))
print('输入：%s %s，输出：%s，答案：%s' % (node1, 7, getKthNode(node1, 7), None))
