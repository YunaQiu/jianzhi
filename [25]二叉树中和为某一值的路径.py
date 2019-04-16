# -*- coding: utf-8 -*-
'''
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
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

class Solution:
    def FindPath(self, root, num):
        if root is None:
            return []
        routeDict = {}
        self.findCore(root, num, routeDict, [], 0)
        keys = sorted(routeDict.keys())
        result = []
        for k in keys[::-1]:
            result.extend(routeDict[k])
        # [print(','.join(x)) for x in result]
        return result

    def findCore(self, node, num, routeDict, tempList, tempSum):
        tempList.append(node.val)
        tempSum += node.val
        if node.left is None and node.right is None and tempSum==num:
            length = len(tempList)
            if length not in routeDict:
                routeDict[length] = [tempList.copy()]
            else:
                routeDict[length].append(tempList.copy())
        if node.left is not None:
            self.findCore(node.left, num, routeDict, tempList, tempSum)
        if node.right is not None:
            self.findCore(node.right, num, routeDict, tempList, tempSum)
        tempList.pop()

'''
思路：用一个字典记录结果列表（key为长度，value为列表），用一个数组记录当前临时路径。采用前序遍历搜索，若是叶子节点且加和等于目标值，则加入字典中，否则返回；若不是叶子节点，则继续向下遍历。遍历完成后，对字典的key进行排序合并输出成结果列表
特殊变体：全为正数（可提前中断遍历），二叉搜索树（可选择遍历方向）
注意：题目没说如果存在相同的两条路径，是否去重
边界：空树，只有左子树有/没有目标值，只有右子树有/没有目标值，有多个目标路径且左子树比右子树路径长/短，有两条相同路径
'''
s = Solution()
print('输入：%s %s' % (None, 1), '输出：%s，答案：%s' % (s.FindPath(None,1), []))
tree1 = TreeNode(1)
print('输入：%s %s' % (tree1, 1), '输出：%s，答案：%s' % (s.FindPath(tree1,1), [[1]]))
tree1.left = tree2 = TreeNode(2)
print('输入：%s %s' % (tree1, 3), '输出：%s，答案：%s' % (s.FindPath(tree1,3), [[1,2]]))
tree2.left = tree3 = TreeNode(3)
print('输入：%s %s' % (tree1, 3), '输出：%s，答案：%s' % (s.FindPath(tree1,3), []))
tree2.right = TreeNode(4)
tree1.right = tree4 = TreeNode(5)
print('输入：%s %s' % (tree1, 6), '输出：%s，答案：%s' % (s.FindPath(tree1,6), [[1,2,3],[1,5]]))
tree4.right = tree5 = TreeNode(1)
print('输入：%s %s' % (tree1, 7), '输出：%s，答案：%s' % (s.FindPath(tree1,7), [[1,2,4],[1,5,1]]))
tree5.left = TreeNode(0)
print('输入：%s %s' % (tree1, 7), '输出：%s，答案：%s' % (s.FindPath(tree1,7), [[1,5,1,0],[1,2,4]]))
tree1.left = None
print('输入：%s %s' % (tree1, 7), '输出：%s，答案：%s' % (s.FindPath(tree1,7), [[1,5,1,0]]))
tree5.right = TreeNode(0)
print('输入：%s %s' % (tree1, 7), '输出：%s，答案：%s' % (s.FindPath(tree1,7), [[1,5,1,0],[1,5,1,0]]))
