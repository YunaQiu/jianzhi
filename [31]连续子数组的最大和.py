# -*- coding: utf-8 -*-
'''
在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和。(子向量的长度至少是1)
'''

def greatestSum(numList):
    if len(numList) == 0:
        return None
    greatest = numList[0]
    addup = 0
    for x in numList:
        sum = addup + x
        if sum > greatest:
            greatest = sum
        addup = max(sum, 0)
    return greatest

'''
思路：设数组的最大和子串从下标i开始，则i之前的数之和必然小于0。因此若遍历时和小于0，则舍弃先前的数从下个数开始找。
边界：空数组，只有1个元素，全部正数，全部负数
'''
print('输入：%s，输出：%s，答案：%s' % ([], greatestSum([]), None))
print('输入：%s，输出：%s，答案：%s' % ([-1], greatestSum([-1]), -1))
print('输入：%s，输出：%s，答案：%s' % ([-1,-2,-5,-1,-4], greatestSum([-1,-2,-5,-1,-4]), -1))
print('输入：%s，输出：%s，答案：%s' % ([1,2,1,3,2], greatestSum([1,2,1,3,2]), 9))
print('输入：%s，输出：%s，答案：%s' % ([1,2,-3,-1,3,-1,2], greatestSum([1,2,-3,-1,3,-1,2]), 4))
