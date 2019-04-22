# -*- coding:utf-8 -*-
'''
希尔排序：插入排序法的改进。每轮对指定步长间隔的数所组成的数组进行直接插入排序，在迭代中不断缩小步长间隔。由于每轮都是对一个基本有序的数组进行排序，从而提高了排序效率。最常见的步长增量序列为希尔增量(n/2,n/4,n/8,...,1)
时间复杂度：与增量序列的选取有关，大致为O(NlogN~N^2)，复杂度与增量的数学关系至今依旧是未解的难题
常见(最坏)复杂度：希尔增量为O(N^2)，Hibbard增量为O(N^(3/2))，Sedgewick增量为O(N^(4/3))
(最坏)复杂度下界：O(NlogN)
空间复杂度：O(1)
稳定性：不稳定
'''

def shellSort(arr):
    if len(arr) < 2:
        return arr
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            for j in range(i-gap, -1, -gap):
                if arr[j] <= arr[j+gap]:
                    break
                arr[j], arr[j+gap] = arr[j+gap], arr[j]
        gap //= 2
    return arr

# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([], shellSort([]), []))
print('输入：%s，输出：%s，答案：%s' % ([2], shellSort([2]), [2]))
print('输入：%s，输出：%s，答案：%s' % ([2,1], shellSort([2,1]), [1,2]))
print('输入：%s，输出：%s，答案：%s' % ([0,1], shellSort([0,1]), [0,1]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1], shellSort([0,3,1]), [0,1,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3], shellSort([0,3,1,3]), [0,1,3,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3,3], shellSort([0,3,1,3,3]), [0,1,3,3,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3,0,3], shellSort([0,3,1,3,0,3]), [0,0,1,3,3,3]))
