# -*- coding: utf-8 -*-
'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''
import random

def smallK(numList, k):
    if k <= 0:
        return []
    numList = list(set(numList))
    if len(numList) < k:
        return []
    if len(numList) == k:
        return numList
    head, tail = 0, len(numList)-1
    while head < tail:
        temp = partSort(numList, head, tail)
        if temp == k or temp == k-1:
            return numList[:k]
        if temp > k:
            tail = temp-1
        else:
            head = temp+1

def partSort(numList, head, tail):
    if head==tail:
        return head
    i = random.randint(head,tail)
    numList[i], numList[tail] = numList[tail], numList[i]
    i, j = head, tail
    while i < j:
        while i < j and numList[i] <= numList[tail]:
            i += 1
        while i < j and numList[j] >= numList[tail]:
            j -= 1
        numList[i], numList[j] = numList[j], numList[i]
    numList[j], numList[tail] = numList[tail], numList[j]
    return j

'''
思路：先去重，然后采用快排思想，找出第k小的数字，输出k之前的数字。
注意：题目没说如果少于k个数字应该怎么处理。另外如果是海量数据，则改成采用最大堆存储最大的k个数字，然后遍历数组。复杂度O(Nlogk)
边界：空数组，k小于等于0，小于k个数字，去重后小于k个数，倒序数组
'''
print('输入：%s %s，输出：%s，答案：%s' % ([], 1, smallK([], 1), []))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2], 0, smallK([1,2], 0), []))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2], 1, smallK([1,2], 1), [1]))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2], 2, smallK([1,2], 2), [1,2]))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2], 3, smallK([1,2], 3), []))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2,2,1,2,2,2], 3, smallK([1,2,2,1,2,2,2], 3), []))
print('输入：%s %s，输出：%s，答案：%s' % ([5,4,3,3,2,1,2], 3, smallK([5,4,3,3,2,1,2], 3), [1,2,3]))
print('输入：%s %s，输出：%s，答案：%s' % ([4,5,1,6,2,7,2,8],2, smallK([4,5,1,6,2,7,2,8],2), [1,2]))
