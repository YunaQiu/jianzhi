# -*- coding: utf-8 -*-
'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        output = ""
        if self.left is not None:
            output += "(%s)<=" % self.left
        output += "%s" % self.val
        if self.right is not None:
            output += "=>(%s)" % self.right
        return output
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None or pRoot2 is None:
            return False
        if self.isSubtree(pRoot1, pRoot2):
            return True
        if self.HasSubtree(pRoot1.left, pRoot2):
            return True
        if self.HasSubtree(pRoot1.right, pRoot2):
            return True
        return False

    def isSubtree(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        if not self.isSubtree(pRoot1.left, pRoot2.left):
            return False
        if not self.isSubtree(pRoot1.right, pRoot2.right):
            return False
        return True

'''
思路：采用前序遍历子树，当根节点值一样时，进一步判断是否是子树，若是则返回true。不是则继续遍历，直到发现子树或遍历完毕为止
边界：空树，空子树，根节点为子树，上层节点值相同但不是子树/下层节点值相同且是子树，子树为母树的中间部分（非叶节点）
'''
# 测试用例
s = Solution()
tree1 = TreeNode(1)
tree1.left = tree2 = TreeNode(2)
tree2.left = tree3 = TreeNode(4)
tree2.right = tree4 = TreeNode(2)
tree4.left = tree5 = TreeNode(5)
tree4.right = tree6 = TreeNode(6)
print('输入：%s %s，输出：%s，答案：%s' % (None, None, s.HasSubtree(None, None), False))
print('输入：%s %s，输出：%s，答案：%s' % (tree1, None, s.HasSubtree(tree1, None), False))
print('输入：%s %s，输出：%s，答案：%s' % (tree1, tree1, s.HasSubtree(tree1, tree1), True))
print('输入：%s %s，输出：%s，答案：%s' % (tree1, tree4, s.HasSubtree(tree1, tree4), True))
tree7 = TreeNode(2)
tree7.right = tree8 = TreeNode(2)
print('输入：%s %s，输出：%s，答案：%s' % (tree1, tree7, s.HasSubtree(tree1, tree7), True))
tree7.left = tree9 = TreeNode(9)
print('输入：%s %s，输出：%s，答案：%s' % (tree1, tree7, s.HasSubtree(tree1, tree7), False))
