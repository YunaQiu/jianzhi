# -*- coding: utf-8 -*-
'''
选择排序法：遍历0~n-1的序列，找到最小的数字，将它与第0位的数字交换。再遍历1~n-1，找到最小的数字与第1位交换...以此类推
时间复杂度：O(N^2)
最优复杂度：O(N^2)
最坏复杂度：O(N^2)
空间复杂度：O(1)
稳定性：不稳定
'''

def selectSort(arr):
    if len(arr) < 2:
        return arr
    for i in range(len(arr)-1):
        minIdx = i
        for j in range(i, len(arr)):
            minIdx = j if arr[j] < arr[minIdx] else minIdx
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr

# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([], selectSort([]), []))
print('输入：%s，输出：%s，答案：%s' % ([1], selectSort([1]), [1]))
print('输入：%s，输出：%s，答案：%s' % ([1,2], selectSort([1,2]), [1,2]))
print('输入：%s，输出：%s，答案：%s' % ([1,2,3], selectSort([1,2,3]), [1,2,3]))
print('输入：%s，输出：%s，答案：%s' % ([3,2,1], selectSort([3,2,1]), [1,2,3]))
print('输入：%s，输出：%s，答案：%s' % ([3,2,0,1], selectSort([3,2,0,1]), [0,1,2,3]))
print('输入：%s，输出：%s，答案：%s' % ([3,1,2,3,1], selectSort([3,1,2,3,1]), [1,1,2,3,3]))
