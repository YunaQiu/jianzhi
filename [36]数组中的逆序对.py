# -*- coding: utf-8 -*-
'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
注：题目保证输入的数组中没有的相同的数字
数据范围：
	对于%50的数据,size<=10^4
	对于%75的数据,size<=10^5
	对于%100的数据,size<=2*10^5
'''

def inversePair(numList):
    if len(numList) <= 1:
        return 0
    inverse = sortCore(numList, 0, len(numList)-1, numList.copy())
    return inverse % 1000000007

def sortCore(numList, start, end, copyList):
    if end == start:
        return 0
    if end - start == 1:
        if numList[start] > numList[end]:
            copyList[start], copyList[end] = numList[end], numList[start]
            return 1
        else:
            return 0

    mid = (start + end) // 2
    inverse = sortCore(copyList, start, mid-1, numList)
    inverse += sortCore(copyList, mid, end, numList)

    p1,p2,pc = start, mid, start
    while p1 < mid and p2 <= end:
        if numList[p2] < numList[p1]:
            copyList[pc] = numList[p2]
            inverse += mid - p1
            p2 += 1
        else:
            copyList[pc] = numList[p1]
            p1 += 1
        pc += 1
    if p1 < mid:
        copyList[pc:end+1] = numList[p1:mid]
    else:
        copyList[pc:end+1] = numList[p2:end+1]
    return inverse


'''
思路：归并排序可以计算逆序对。初始化时不断对半分组，直至组中元素个数为1或2。对组内元素进行排序并计算逆序对。再对相邻组间合并排序，同时计算逆序对。
备注：该python版本在牛客上显示超时，但牛客上那些提交成功的python版本在我提交时同样显示超时，且本地测试结果显示我的版本运行时间比牛客上别人的版本还快了0.5秒（总共1.3秒）
边界：元素个数：0,1,2,3，奇数、偶数个数，全逆，顺序，长度大数2*10^5
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([], inversePair([]), 0))
print('输入：%s，输出：%s，答案：%s' % ([1], inversePair([1]), 0))
print('输入：%s，输出：%s，答案：%s' % ([1,2], inversePair([1,2]), 0))
print('输入：%s，输出：%s，答案：%s' % ([2,1], inversePair([2,1]), 1))
print('输入：%s，输出：%s，答案：%s' % ([1,2,0], inversePair([1,2,0]), 2))
print('输入：%s，输出：%s，答案：%s' % ([3,2,1,0], inversePair([3,2,1,0]), 6))
print('输入：%s，输出：%s，答案：%s' % ([1,2,3,4,5,6,7,0], inversePair([1,2,3,4,5,6,7,0]), 7))
print('输入：%s，输出：%s，答案：%s' % ('0~2*10^5', inversePair(list(range(2*10**5))), 0))
print('输入：%s，输出：%s，答案：%s' % ('2*10^5~0', inversePair(list(range(2*10**5,-1,-1))), '?'))
