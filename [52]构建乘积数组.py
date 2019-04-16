# -*- coding: utf-8 -*-
'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''

def multiArr(arrA):
    if len(arrA) == 0:
        return []
    if len(arrA) == 1:
        return [1]
    arrB = [1]*len(arrA)
    for i in range(1,len(arrA)):
        arrB[i] = arrB[i-1] * arrA[i-1]
    temp = 1
    for i in range(len(arrA)-2,-1,-1):
        temp *= arrA[i+1]
        arrB[i] *= temp
    return arrB

'''
思路：用两个n维的辅助数组M1和M2，M1中每个元素M1[i]=A[0]*~A[i]，M2中每个元素M2[i]=A[i]*~A[n-1]，则B[i]=M1[i-1]*M2[i+1]，总共遍历3次，复杂度O(N)
优化：可以不用辅助空间直接构建数组B，思路一致，只不过先从前往后遍历计算前半段的值，然后从后往前遍历计算后半段的值并更新到数组中。
边界：数组A的长度为0,1,2,3，数组中有0，有正负数
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([], multiArr([]), []))
print('输入：%s，输出：%s，答案：%s' % ([2], multiArr([2]), [1]))
print('输入：%s，输出：%s，答案：%s' % ([1,2], multiArr([1,2]), [2,1]))
print('输入：%s，输出：%s，答案：%s' % ([1,2,-3], multiArr([1,2,-3]), [-6,-3,2]))
print('输入：%s，输出：%s，答案：%s' % ([1,2,0,-3], multiArr([1,2,0,-3]), [0,0,-6,0]))
