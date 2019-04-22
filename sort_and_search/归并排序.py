# -*- coding:utf-8 -*-
'''
归并排序法：采用分治法思想，从最小的二元组开始，每次将两个已经排好序的序列合并成一个排序序列。
时间复杂度：O(NlogN)
最优复杂度：O(NlogN)
最坏复杂度：O(NlogN)
空间复杂度：O(N)
稳定性：稳定
'''

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(arr1, arr2):
    i = j = 0
    arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    arr.extend(arr1[i:])
    arr.extend(arr2[j:])
    return arr

# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([], mergeSort([]), []))
print('输入：%s，输出：%s，答案：%s' % ([2], mergeSort([2]), [2]))
print('输入：%s，输出：%s，答案：%s' % ([2,1], mergeSort([2,1]), [1,2]))
print('输入：%s，输出：%s，答案：%s' % ([0,1], mergeSort([0,1]), [0,1]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1], mergeSort([0,3,1]), [0,1,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3], mergeSort([0,3,1,3]), [0,1,3,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3,3], mergeSort([0,3,1,3,3]), [0,1,3,3,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3,0,3], mergeSort([0,3,1,3,0,3]), [0,0,1,3,3,3]))
