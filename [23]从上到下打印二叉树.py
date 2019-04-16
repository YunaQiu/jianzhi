# -*- coding: utf-8 -*-
'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
注意：牛客网上是要求返回节点值的序列
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

def printTree(tree):
    if tree is None:
        return []
    queue = [tree]
    printList = []
    while len(queue) > 0:
        node = queue.pop(0)
        printList.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    # 打印
    # [print(x) for x in printList]
    return printList

'''
思路：建一个队列，从根节点开始，每次打印队首节点，同时将该节点的左右节点放入队尾中
边界：空树，只有一个根节点，只有左子树，只有右子树，满树
'''
tree1 = TreeNode(1)
print('输入：%s' % None, '输出：%s' % printTree(None))
print('输入：%s' % tree1, '输出：%s' % printTree(tree1))
tree1.left = tree2 = TreeNode(2)
tree2.left = tree3 = TreeNode(3)
print('输入：%s' % tree1, '输出：%s' % printTree(tree1))
tree2.right = tree5 = TreeNode(5)
print('输入：%s' % tree1, '输出：%s' % printTree(tree1))
tree1.right = tree4 = TreeNode(4)
tree4.left = TreeNode(5)
tree4.right = TreeNode(6)
print('输入：%s' % tree1, '输出：%s' % printTree(tree1))
tree1.left = None
print('输入：%s' % tree1, '输出：%s' % printTree(tree1))
tree4.left = None
print('输入：%s' % tree1, '输出：%s' % printTree(tree1))
