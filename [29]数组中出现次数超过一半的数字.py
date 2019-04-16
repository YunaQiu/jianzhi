# -*- coding: utf-8 -*-
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
import random
def findNum(numList):
    if len(numList) == 0:
        return 0
    if len(numList) == 1:
        return numList[0]
    head, tail, mid = 0, len(numList)-1, (len(numList) - 1) // 2
    while head <= tail:
        k = partition(numList, head, tail)
        if k == mid:
            return numList[k] if isMoreThanHalf(numList, numList[k]) else 0
        if k < mid:
            head = k+1
        else:
            tail = k-1
    return 0

def partition(numL, head, tail):
    if head == tail:
        return head
    i = random.randint(head, tail)
    numL[i], numL[tail] = numL[tail], numL[i]
    i,j = head,tail
    while i < j:
        while i < j and numL[i] <= numL[tail]:
            i += 1
        while i < j and numL[j] >= numL[tail]:
            j -= 1
        numL[i], numL[j] = numL[j], numL[i]
    numL[j], numL[tail] = numL[tail], numL[j]
    return j

def isMoreThanHalf(numList, num):
    count = 0
    for x in numList:
        if x == num:
            count += 1
    return count > len(numList) / 2

'''
思路：题目相当于要找数组的中位数。而快排可以用O(N)复杂度解决数组中第k大元素的问题。此外找到中位数后，还要判断它的次数是否超过一半
边界：空数组，1/2/3个数字，中位数堆积在前半段/后半段，不存在超过一半的
'''
print('输入：%s，输出：%s，答案：%s' % ([], findNum([]), 0))
print('输入：%s，输出：%s，答案：%s' % ([1], findNum([1]), 1))
print('输入：%s，输出：%s，答案：%s' % ([1,2], findNum([1,2]), 0))
print('输入：%s，输出：%s，答案：%s' % ([2,2], findNum([2,2]), 2))
print('输入：%s，输出：%s，答案：%s' % ([2,1,2], findNum([2,1,2]), 2))
print('输入：%s，输出：%s，答案：%s' % ([2,2,2,1,3,3], findNum([2,2,2,1,3,3]), 0))
print('输入：%s，输出：%s，答案：%s' % ([2,2,2,2,3,3], findNum([2,2,2,2,3,3]), 2))
print('输入：%s，输出：%s，答案：%s' % ([2,1,3,3,3,3], findNum([2,1,3,3,3,3]), 3))
