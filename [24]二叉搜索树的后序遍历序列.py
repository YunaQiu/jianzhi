# -*- coding: utf-8 -*-
'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''

def isBST(nodeList):
    if len(nodeList) == 0:
        return False
    if len(nodeList) == 1:
        return True
    root = nodeList[-1]
    rightIdx = 0
    while nodeList[rightIdx] <= root:
        rightIdx += 1
        if rightIdx == len(nodeList)-1:
            break
    for i in range(rightIdx, len(nodeList)-1):
        if nodeList[i] < root:
            return False
    left = isBST(nodeList[0:rightIdx]) if rightIdx>0 else True
    right = isBST(nodeList[rightIdx:-1]) if rightIdx<len(nodeList)-1 else True
    return left and right

'''
思路：序列的最后一个值为根节点。因此对序列从前往后扫描，第一个大于根节点的值即是右子树的开始的位置。继续向后扫描，若出现小于根节点的值，则不可能是平衡树。依次递归各子节点
边界；空树(题目未说清楚是true还是false)，只有一个根节点，只有左子树，只有右子树
'''
print('输入：%s，输出：%s，答案：%s' % ([], isBST([]), False))
print('输入：%s，输出：%s，答案：%s' % ([1], isBST([1]), True))
print('输入：%s，输出：%s，答案：%s' % ([1,2,3,4], isBST([1,2,3,4]), True))
print('输入：%s，输出：%s，答案：%s' % ([1,3,2,4], isBST([1,3,2,4]), True))
print('输入：%s，输出：%s，答案：%s' % ([4,3,2,1], isBST([4,3,2,1]), True))
print('输入：%s，输出：%s，答案：%s' % ([2,4,1,3], isBST([2,4,1,3]), False))
print('输入：%s，输出：%s，答案：%s' % ([2,4,1,3], isBST([2,4,1,3]), False))
