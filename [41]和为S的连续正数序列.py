# -*- coding: utf-8 -*-
'''
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
import math
def findNumSeq(tsum):
    maxLen = int(math.sqrt(2*tsum))
    result = []
    for l in range(maxLen, 1, -1):
        mid = tsum / l      #python2: mid = float(tsum) / l
        if mid == int(mid) and l % 2 == 1:
            result.append([i for i in range(int(mid - (l-1)/2), int(mid + (l+1)/2))])
        elif mid - int(mid) == 0.5 and l % 2 == 0:
            result.append([i for i in range(int(mid + 0.5 - l/2), int(mid + 0.5 + l/2))])
    return result


'''
思路：对于整数n，若存在序列长度为偶数x，则n/x的小数部分必然为0.5，且n/x>x/2；若序列长度为奇数x，则n/x必然为整数，且n/x>x/2。加上题目的序列顺序要求，可求出x的上限，从大到小遍历求解所有可能序列。
边界：只有x=2的序列（3），只有x=3的序列（6），多种可能序列但x并非全部满足（100）
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % (3, findNumSeq(3), [[1,2]]))
print('输入：%s，输出：%s，答案：%s' % (6, findNumSeq(6), [[1,2,3]]))
print('输入：%s，输出：%s，答案：%s' % (15, findNumSeq(15), [[1,2,3,4,5],[4,5,6],[7.8]]))
print('输入：%s，输出：%s，答案：%s' % (100, findNumSeq(100), '?'))
