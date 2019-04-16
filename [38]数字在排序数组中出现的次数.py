# -*- coding: utf-8 -*-
'''
统计一个数字在排序数组中出现的次数。
'''

def findCount(numList, num):
    if len(numList) == 0:
        return 0
    start = findIdx(numList, num, 0, len(numList)-1)
    if start is None:
        return 0
    elif start == len(numList)-1 or numList[start+1]>num:
        return 1
    end = findIdx(numList, num, 0, len(numList)-1, False)
    return end - start + 1

def findIdx(numList, num, start, end, findStart=True):
    if start == end:
        return start if numList[start] == num else None
    if numList[start] > num or numList[end] < num:
        return None
    mid = (start + end) // 2
    if findStart:
        if numList[start] == num:
            return start
        if len(numList) == 2 and numList[end] == num:
            return end
        if numList[mid] == num and numList[mid-1] < num:
            return mid
        if numList[mid] >= num:
            return findIdx(numList, num, start, mid-1)
        else:
            return findIdx(numList, num, mid+1, end)
    else:
        if numList[end] == num:
            return end
        if len(numList) == 2 and numList[start] == num:
            return start
        if numList[mid] == num and numList[mid+1] > num:
            return mid
        if numList[mid] > num:
            return findIdx(numList, num, start, mid-1, False)
        else:
            return findIdx(numList, num, mid+1, end, False)


'''
思路：采用二分查找法，找到数字的起始位置和结束位置，相减得到次数
边界：数组长度为0、1、2、3，整个数组都是目标数字，数字起始位置在数组开头，结束位置在数组末尾，位置在中间，数组中只有一个数字，数组中没有数字
'''
# 测试用例
print('输入：%s %s，输出：%s，答案：%s' % ([], 1, findCount([], 1), 0))
print('输入：%s %s，输出：%s，答案：%s' % ([1], 1, findCount([1], 1), 1))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2], 1, findCount([1,2], 1), 1))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2,3], 0, findCount([1,2,3], 0), 0))
print('输入：%s %s，输出：%s，答案：%s' % ([1,1,2,3], 1, findCount([1,1,2,3], 1), 2))
print('输入：%s %s，输出：%s，答案：%s' % ([1,1,2,3,3], 3, findCount([1,1,2,3,3], 3), 2))
print('输入：%s %s，输出：%s，答案：%s' % ([1,1,2,3,3], 2, findCount([1,1,2,3,3], 2), 1))
print('输入：%s %s，输出：%s，答案：%s' % ([1,1,2,2,3,3], 2, findCount([1,1,2,2,3,3], 2), 2))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2,3,3,3,3,4,5], 3, findCount([1,2,3,3,3,3,4,5], 3), 4))
