# -*- coding: utf-8 -*-
'''
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
注意：返回二维列表，如[[1],[3,2],[4,5,6,7]]
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

def zPrintTree(tree):
    if tree is None:
        return []
    lStack = [tree]
    rStack = []
    printList = []
    while len(lStack) > 0 or len(rStack) > 0:
        tempList = []
        while len(lStack) > 0:
            node = lStack.pop()
            tempList.append(node.val)
            if node.left is not None:
                rStack.append(node.left)
            if node.right is not None:
                rStack.append(node.right)
        if len(tempList) > 0:
            printList.append(tempList)
            tempList = []
        while len(rStack) > 0:
            node = rStack.pop()
            tempList.append(node.val)
            if node.right is not None:
                lStack.append(node.right)
            if node.left is not None:
                lStack.append(node.left)
        if len(tempList) > 0:
            printList.append(tempList)
    return printList

'''
思路：利用两个栈存储下一行的节点序列，从左到右读取结点时，依次往栈中压入左结点和右节点。待该行节点读取完后，再从栈中一次弹出读取下一行节点（即从右到左），同时依次往另一个栈压入右节点和左节点，如此循环。
边界：空树，单数层，双数层，只有单边节点，满树
'''
print('输入：%s，输出：%s，答案：%s' % (None, zPrintTree(None), []))
node1 = TreeNode(1)
print('输入：%s，输出：%s，答案：%s' % (node1, zPrintTree(node1), [[1]]))
node2 = node1.left = TreeNode(2)
node3 = node1.right = TreeNode(3)
print('输入：%s，输出：%s，答案：%s' % (node1, zPrintTree(node1), [[1],[3,2]]))
node4 = node2.left = TreeNode(4)
node5 = node3.right = TreeNode(5)
print('输入：%s，输出：%s，答案：%s' % (node1, zPrintTree(node1), [[1],[3,2],[4,5]]))
node6 = node2.right = TreeNode(6)
node7 = node3.left = TreeNode(7)
print('输入：%s，输出：%s，答案：%s' % (node1, zPrintTree(node1), [[1],[3,2],[4,6,7,5]]))
