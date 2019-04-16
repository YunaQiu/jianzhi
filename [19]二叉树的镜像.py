# -*- coding: utf-8 -*-
'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''
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

def mirror(tree):
    if tree is None:
        return None
    if tree.left is not None or tree.right is not None:
        temp = tree.left
        tree.left = tree.right
        tree.right = temp
    mirror(tree.left)
    mirror(tree.right)
    return tree

'''
思路：先对调根节点的左右子树位置，再遍历翻转两个左右子树
边界：空树，只有一个结点，只有左节点，只有右节点，完全二叉树，其他二叉树
'''
# 测试用例
tree1 = TreeNode(1)
print('输入：%s' % None, '输出：%s' % mirror(None))
print('输入：%s' % tree1, '输出：%s' % mirror(tree1))
tree1.left = tree2 = TreeNode(2)
tree2.left = tree3 = TreeNode(3)
print('输入：%s' % tree1, '输出：%s' % mirror(tree1))
print('输入：%s' % tree1, '输出：%s' % mirror(tree1))
tree1.right = tree4 = TreeNode(4)
tree4.left = TreeNode(5)
tree4.right = TreeNode(6)
print('输入：%s' % tree1, '输出：%s' % mirror(tree1))
tree2.left = TreeNode(7)
print('输入：%s' % tree1, '输出：%s' % mirror(tree1))
