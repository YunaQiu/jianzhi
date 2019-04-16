# -*- coding:utf-8 -*-
'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
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

def treeConstruct(foreList, midList):
    '''
    若树为空返回None
    否则返回树的根节点
    '''
    if len(foreList) == 0:
        return None
    root = TreeNode(foreList[0])
    loc = midList.index(foreList[0])
    if loc > 0:
        root.left = treeConstruct(foreList[1:loc+1], midList[:loc])
    if loc < len(midList) - 1:
        root.right = treeConstruct(foreList[loc+1:], midList[loc+1:])
    return root

'''
思路：前序的第一个节点为根结点，在中序中找到这个结点，则结点左边为左子树序列，右边为右子树序列，依次递归
边界判定：
输入空序列，序列只有一个节点
只有左子树/只有右子树
'''
# 测试用例
print('输入：%s %s\t 输出：%s\t 答案：%s' % ([], [], treeConstruct([], []), "None"))
print('输入：%s %s\t 输出：%s\t 答案：%s' % ([1], [1], treeConstruct([1], [1]), "1"))
print('输入：%s %s\t 输出：%s\t 答案：%s' % ([1,2,4,5,3,6,7], [4,2,5,1,6,3,7], treeConstruct([1,2,4,5,3,6,7], [4,2,5,1,6,3,7]), "((4)<=2=>(5))<=1=>((6)<=3=>(7))"))
print('输入：%s %s\t 输出：%s\t 答案：%s' % ([1,2,4], [4,2,1], treeConstruct([1,2,4], [4,2,1]), "((4)<=2)<=1"))
print('输入：%s %s\t 输出：%s\t 答案：%s' % ([1,3,7], [1,3,7], treeConstruct([1,3,7], [1,3,7]), "(1=>(3=>(7))"))
print('输入：%s %s\t 输出：%s\t 答案：%s' % ([1,2,4,5], [4,2,5,1], treeConstruct([1,2,4,5], [4,2,5,1]), "((4)<=2=>(5))<=1"))
