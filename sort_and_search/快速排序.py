# -*- coding: utf-8 -*-
'''
快速排序法：从数组中选取一个数作为基准，将小于基准的数放在基准左边，大于基准的数放在右面，称为一次分区操作。然后递归排序基准左边的子序列和右边的子序列。
基准选取改进：为避免基本有序的数组影响排序效率，基准值的选取可以是取随机数、取中间数、取前中后三个数中的中值。
时间复杂度：O(NlogN)
最优复杂度：O(NlogN)
最坏复杂度：O(N^2)
空间复杂度：O(1ogN)   //因为每一层递归都要记录下基准点排序后的位置
稳定性：不稳定
'''

import random

def quickSort(arr, start=0, end=None):
    end = len(arr)-1 if end is None else end
    if start >= end:
        return arr
    flag = partition(arr, start, end)
    quickSort(arr, start, flag-1)
    quickSort(arr, flag+1, end)
    return arr

def partition(arr, start, end):
    randIdx = random.randint(start, end)
    arr[randIdx], arr[end] = arr[end], arr[randIdx]
    largeIdx = start
    for i in range(start, end):
        if arr[i] > arr[end]:
            continue
        if largeIdx < i:
            arr[largeIdx], arr[i] = arr[i], arr[largeIdx]
        largeIdx += 1
    arr[largeIdx], arr[end] = arr[end], arr[largeIdx]
    return largeIdx

# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([], quickSort([]), []))
print('输入：%s，输出：%s，答案：%s' % ([2], quickSort([2]), [2]))
print('输入：%s，输出：%s，答案：%s' % ([2,1], quickSort([2,1]), [1,2]))
print('输入：%s，输出：%s，答案：%s' % ([0,1], quickSort([0,1]), [0,1]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1], quickSort([0,3,1]), [0,1,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3], quickSort([0,3,1,3]), [0,1,3,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3,3], quickSort([0,3,1,3,3]), [0,1,3,3,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3,0,3], quickSort([0,3,1,3,0,3]), [0,0,1,3,3,3]))
