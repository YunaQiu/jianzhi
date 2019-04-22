# -*- coding:utf-8 -*-
'''
基数排序：假设数字由若干位组成，最大的数字有d位，每一位的取值范围为radix（可以理解为进制）。从最低位开始，依次将每一位当做排序关键字对数字进行分桶排序，若位数不够则补0，直到排序完最高位后，数组便是有序的。
时间复杂度：O(d(N+r))
空间复杂度：O(N+r)
稳定性：稳定
'''

import math
def radixSort(arr, radix=10):
    if len(arr) < 2:
        return arr
    d = math.ceil(math.log(max(arr), radix))
    bucket = [[] for i in range(radix)]
    for i in range(d):
        for x in arr:
            bucket[(x // (radix**i)) % radix].append(x)
        arr.clear()
        for i in range(radix):
            arr.extend(bucket[i])
            bucket[i] = []
    return arr

# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([], radixSort([]), []))
print('输入：%s，输出：%s，答案：%s' % ([2], radixSort([2]), [2]))
print('输入：%s，输出：%s，答案：%s' % ([2,1], radixSort([2,1]), [1,2]))
print('输入：%s，输出：%s，答案：%s' % ([0,10], radixSort([0,10]), [0,10]))
print('输入：%s，输出：%s，答案：%s' % ([0,30,1], radixSort([0,30,1]), [0,1,30]))
print('输入：%s，输出：%s，答案：%s' % ([0,30,10,30], radixSort([0,30,10,30]), [0,10,30,30]))
print('输入：%s，输出：%s，答案：%s' % ([0,30,10,30,3], radixSort([0,30,10,30,3]), [0,3,10,30,30]))
print('输入：%s，输出：%s，答案：%s' % ([0,30,10,3,0,30], radixSort([0,30,10,3,0,30]), [0,0,3,10,30,30]))
