# -*- coding: utf-8 -*-
'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。
'''

def findNumsSumS(numList, tsum):
    i,j = 0, len(numList)-1
    while i<j:
        temp = numList[i] + numList[j]
        if temp == tsum:
            return [numList[i], numList[j]]
        if temp < tsum:
            i += 1
        else:
            j -= 1
    return []

'''
思路：两个指针，从两边向中间遍历。当和小于s时，头部头部指针向后移。当和大于s时，尾部指针向前移。找到的第一对符合条件的数，就是乘积最小的数。
边界：只有两个数字，有三个数字，有不止一对，其中一对数符号不同，一对数符号相同
'''
# 测试用例
print('输入：%s %s，输出%s，答案：%s' % ([1,2], 3, findNumsSumS([1,2], 3), [1,2]))
print('输入：%s %s，输出%s，答案：%s' % ([-1,1,2], 0, findNumsSumS([-1,1,2], 0), [-1,1]))
print('输入：%s %s，输出%s，答案：%s' % ([-2,-1,1,2], 0, findNumsSumS([-2,-1,1,2], 0), [-2,2]))
print('输入：%s %s，输出%s，答案：%s' % ([-2,-1,0,1,2], 1, findNumsSumS([-2,-1,0,1,2], 1), [-1,2]))
