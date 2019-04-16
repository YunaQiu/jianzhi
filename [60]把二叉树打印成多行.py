# -*- coding: utf-8 -*-
'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
注意：返回二维列表[[1,2],[4,5]]
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
        tempList = []
        for i in range(len(queue)):
            t = queue.pop(0)
            tempList.append(t.val)
            if t.left is not None:
                queue.append(t.left)
            if t.right is not None:
                queue.append(t.right)
        printList.append(tempList)
    return printList

'''
思路：用一个队列存储未打印节点，每次从队头取出并打印节点后，将该节点的左节点和右节点存入队尾中，直至队列为空。为了确保能区分每层的节点，需按层进行遍历，每次遍历前记录下队列中的数目，即该层的节点数
边界：空树，只有根节点，只有左节点，只有右节点，都有
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % (None, printTree(None), []))
node1 = TreeNode(1)
print('输入：%s，输出：%s，答案：%s' % (node1, printTree(node1), [[1]]))
node2 = node1.left = TreeNode(2)
print('输入：%s，输出：%s，答案：%s' % (node1, printTree(node1), [[1],[2]]))
node3 = node2.left = TreeNode(3)
print('输入：%s，输出：%s，答案：%s' % (node1, printTree(node1), [[1],[2],[3]]))
node1.left = None
node1.right = node2
print('输入：%s，输出：%s，答案：%s' % (node1, printTree(node1), [[1],[2],[3]]))
node4 = node1.left = TreeNode(4)
print('输入：%s，输出：%s，答案：%s' % (node1, printTree(node1), [[1],[4,2],[3]]))
node5 = node2.right = TreeNode(5)
print('输入：%s，输出：%s，答案：%s' % (node1, printTree(node1), [[1],[4,2],[3,5]]))
node6 = node4.right = TreeNode(6)
print('输入：%s，输出：%s，答案：%s' % (node1, printTree(node1), [[1],[4,2],[6,3,5]]))
