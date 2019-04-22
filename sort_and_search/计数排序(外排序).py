# -*- coding:utf-8 -*-
'''
计数排序：遍历数组找出最大值与最小值，根据他们的差值建立相应长度的辅助数组C，记录数组中每一种取值的元素个数。再对数组C求计数累加，得到的就是对应取值元素排序后的下标位。最后再反向填充得到排序后的数组。本质上是用空间换时间的算法。
时间复杂度：O(N+K)
空间复杂度：O(K)
稳定性：稳定
'''

def countSort(arr):
    if len(arr) < 2:
        return arr
    maxNum = minNum = arr[0]
    for x in arr:
        maxNum = x if x > maxNum else maxNum
        minNum = x if x < minNum else minNum
    countArr = [0] * (maxNum - minNum + 1)
    for x in arr:
        countArr[x - minNum] += 1
    for i in range(1, len(countArr)):
        countArr[i] += countArr[i-1]
    resArr = [None] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        pos = countArr[arr[i]-minNum]
        resArr[pos-1] = arr[i]
        countArr[arr[i]-minNum] -= 1
    return resArr


# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([], countSort([]), []))
print('输入：%s，输出：%s，答案：%s' % ([2], countSort([2]), [2]))
print('输入：%s，输出：%s，答案：%s' % ([2,1], countSort([2,1]), [1,2]))
print('输入：%s，输出：%s，答案：%s' % ([0,1], countSort([0,1]), [0,1]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1], countSort([0,3,1]), [0,1,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3], countSort([0,3,1,3]), [0,1,3,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3,3], countSort([0,3,1,3,3]), [0,1,3,3,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3,0,3], countSort([0,3,1,3,0,3]), [0,0,1,3,3,3]))
