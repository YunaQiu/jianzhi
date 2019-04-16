# -*- coding: utf-8 -*-

'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''

def jumpFloor(number):
    if number <= 2:
        return number
    i,j,k,result = 1,2,2,2
    while k < number:
        result = i + j
        i = j
        j = result
        k += 1
    return result

'''
思路：设跳上第n级台阶的函数为f(x)，则可以分为两种跳法，一种是先跳上n-1级台阶，再跳上1级台阶；一种是先跳上n-2级台阶，再跳上2级台阶。于是f(x)=f(x-1)+f(x-2)，是斐波那契数列。
边界：
0、1、2、3
38/39/40（得数约为INT_MAX)
'''
# 测试用例
print('输入：%s\t输出：%s\t答案：%s' % (0, jumpFloor(0), 0))
print('输入：%s\t输出：%s\t答案：%s' % (1, jumpFloor(1), 1))
print('输入：%s\t输出：%s\t答案：%s' % (2, jumpFloor(2), 2))
print('输入：%s\t输出：%s\t答案：%s' % (3, jumpFloor(3), 3))
print('输入：%s\t输出：%s\t答案：%s' % (38, jumpFloor(38), 63245986))
print('输入：%s\t输出：%s\t答案：%s' % (39, jumpFloor(39), 102334155))
print('输入：%s\t输出：%s\t答案：%s' % (40, jumpFloor(40), 165580141))
