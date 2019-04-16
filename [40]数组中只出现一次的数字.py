# -*- coding: utf-8 -*-
'''
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
返回[a,b] 其中ab是出现一次的两个数字
'''

def findNumAppearOnes(numList):
    result = 0
    for x in numList:
        result ^= x
    split = result & (result-1)
    split = result - split
    num1 = num2 = 0
    for x in numList:
        if x & split == 0:
            num1 ^= x
        else:
            num2 ^= x
    return [num1, num2]


'''
思路：能够区分出现奇偶次的运算符是异或，即对整个数组做异或，除了那两个数字外，其他数字均被抵消。异或结果中，为1的位即为两个数不同的位，按该位为1还是0，将数组分成两部分，再对两个子数组分别求异或，结果即为待求的两个数字。
边界：只有2个数字，数组中有正负数，两个数字的二进制所有位均不同（如0、-1），两个数字中包含0，两个数字中有正负数且形式正好互补
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([1,2], findNumAppearOnes([1,2]), [1,2]))
print('输入：%s，输出：%s，答案：%s' % ([1,2,-1,-2,-1,2], findNumAppearOnes([1,2,-1,-2,1,-2]), [1,-2]))
print('输入：%s，输出：%s，答案：%s' % ([1,1,2,21,3,10,2,3], findNumAppearOnes([1,1,2,21,3,10,2,3]), [21,10]))
print('输入：%s，输出：%s，答案：%s' % ([1,1,2,21,3,-22,2,3], findNumAppearOnes([1,1,2,21,3,-22,2,3]), [21,-22]))
print('输入：%s，输出：%s，答案：%s' % ([1,1,2,0,3,-22,2,3], findNumAppearOnes([1,1,2,0,3,-22,2,3]), [0,-22]))
print('输入：%s，输出：%s，答案：%s' % ([1,1,2,0,3,-1,2,3], findNumAppearOnes([1,1,2,0,3,-1,2,3]), [0,-1]))
