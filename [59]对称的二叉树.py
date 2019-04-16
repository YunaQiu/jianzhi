# -*- coding: utf-8 -*-
'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
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

def isSymmetrical(tree):
    return isMirror(tree.left, tree.right)

def isMirror(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None or tree1.val != tree2.val:
        return False
    return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)

'''
思路：若一个树为对称的，则其左子树和右子树互为镜像。同样左子树的左子树跟右子树的右子树也互为镜像，可以递归求解。
边界：空树，只有根节点，左右子树结构对称但值不同，左右子树结构不对称
注意：牛客上对于空树的判断是True
'''
print('输入：%s，输出：%s，答案：%s' % (None, isSymmetrical(None), True))
node1 = TreeNode(1)
print('输入：%s，输出：%s，答案：%s' % (node1, isSymmetrical(node1), True))
node2 = node1.left = TreeNode(2)
print('输入：%s，输出：%s，答案：%s' % (node1, isSymmetrical(node1), False))
node3 = node1.right = TreeNode(3)
print('输入：%s，输出：%s，答案：%s' % (node1, isSymmetrical(node1), False))
node3.val = 2
print('输入：%s，输出：%s，答案：%s' % (node1, isSymmetrical(node1), True))
node4 = node2.left = TreeNode(4)
node5 = node3.left = TreeNode(4)
print('输入：%s，输出：%s，答案：%s' % (node1, isSymmetrical(node1), False))
node3.left = None
node3.right = node5
print('输入：%s，输出：%s，答案：%s' % (node1, isSymmetrical(node1), True))
node6 = node2.right = TreeNode(6)
print('输入：%s，输出：%s，答案：%s' % (node1, isSymmetrical(node1), False))
node7 = node3.left = TreeNode(6)
print('输入：%s，输出：%s，答案：%s' % (node1, isSymmetrical(node1), True))
