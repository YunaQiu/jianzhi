# -*- coding:utf-8 -*-
'''
二分查找法：首先要求表中的关键字已经是有序排列。采用折半查找方式，每次取中间的数与待查找的元素对比，若小于目标值则在右半边查找，否则则在左半边查找，直至找到目标值或者发现目标值不存在为止。
时间复杂度：O(logN)
'''

def binarySearch(arr, val):
    st, end = 0, len(arr)-1
    while st <= end:
        mid = (st+end) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            st = mid+1
        else:
            end = mid-1
    return None

# 测试用例
print('输入：%s %s，输出：%s，答案：%s' % ([], 2, binarySearch([], 2), None))
print('输入：%s %s，输出：%s，答案：%s' % ([2], 2, binarySearch([2], 2), 0))
print('输入：%s %s，输出：%s，答案：%s' % ([2], 1, binarySearch([2], 1), None))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2], 1, binarySearch([1,2], 1), 0))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2], 2, binarySearch([1,2], 2), 1))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2,3], 1, binarySearch([1,2,3], 1), 0))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2,3,4], 1, binarySearch([1,2,3,4], 1), 0))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2,3,4], 3, binarySearch([1,2,3,4], 3), 2))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2,3,4], 4, binarySearch([1,2,3,4], 4), 3))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2,3,4], 3.5, binarySearch([1,2,3,4], 3.5), None))
