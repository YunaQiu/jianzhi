# -*- coding:utf-8 -*-
'''
插入排序法：从前往后遍历数组。假设数组的前i-1个数有序，对于第i个数，依次往前与前面的数比较并交换，直至找到对应的顺序位置。
时间复杂度：O(N^2)
最优复杂度：O(N)
最坏复杂度：O(N^2)
空间复杂度：O(1)
稳定性：稳定
'''

def insertSort(arr):
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] <= arr[j+1]:
                break
            arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([], insertSort([]), []))
print('输入：%s，输出：%s，答案：%s' % ([2], insertSort([2]), [2]))
print('输入：%s，输出：%s，答案：%s' % ([2,1], insertSort([2,1]), [1,2]))
print('输入：%s，输出：%s，答案：%s' % ([0,1], insertSort([0,1]), [0,1]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1], insertSort([0,3,1]), [0,1,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3], insertSort([0,3,1,3]), [0,1,3,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3,3], insertSort([0,3,1,3,3]), [0,1,3,3,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3,0,3], insertSort([0,3,1,3,0,3]), [0,0,1,3,3,3]))
