# -*- coding: utf-8 -*-
'''
冒泡排序法：从头到尾遍历一次n维数组，对比两两相邻数字，若前面比后面大则交换位置。一遍后最大的数字位于最末尾。然后再次遍历前面n-1个数字。直至全部排序完毕。（从尾到头也是可以的，此时一遍后是最小的数字位于开头）
改进版：设置标志位记录是否发生了交换，若该轮没有发生交换，则提前退出循环。
个人改进2版：每轮记录下最后一次发生交换的位置，下次遍历只遍历到交换位。若一次遍历中没有发生交换，则退出循环。
时间复杂度：O(N^2)
最优复杂度：O(N)  //限改进后的
最差复杂度：O(N^2)
空间复杂度：O(1)
稳定性：稳定
'''
# 经典版
def bubbleSort(numList):
    if len(numList) <= 1:
        return numList
    for i in range(len(numList)-1):
        for j in range(len(numList)-1-i):
            if numList[j] > numList[j+1]:
                numList[j], numList[j+1] = numList[j+1], numList[j]
    return numList

# 改进2版
def bubbleSort2(numList):
    if len(numList) <= 1:
        return numList
    lastExc = len(numList) - 1
    while lastExc > 0:
        temp = lastExc
        for i in range(lastExc):
            if numList[i] > numList[i+1]:
                numList[i], numList[i+1] = numList[i+1], numList[i]
                lastExc = i
        if temp == lastExc:
            break
    return numList


# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([], bubbleSort([]), []))
print('输入：%s，输出：%s，答案：%s' % ([1], bubbleSort([1]), [1]))
print('输入：%s，输出：%s，答案：%s' % ([4,1], bubbleSort([4,1]), [1,4]))
print('输入：%s，输出：%s，答案：%s' % ([1,2,4], bubbleSort([1,2,4]), [1,2,4]))
print('输入：%s，输出：%s，答案：%s' % ([1,2,4,1], bubbleSort([1,2,4,1]), [1,1,2,4]))
print('输入：%s，输出：%s，答案：%s' % ([5,4,4,1], bubbleSort([5,4,4,1]), [1,4,4,5]))
print('输入：%s，输出：%s，答案：%s' % ([5,1,2,3], bubbleSort([5,1,2,3]), [1,2,3,5]))
print('输入：%s，输出：%s，答案：%s' % ([5,4,2,3], bubbleSort([5,4,2,3]), [2,3,4,5]))
