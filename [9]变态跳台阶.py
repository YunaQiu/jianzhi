# -*- coding: utf-8 -*-

'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

def jumpFloor(number):
    if number <= 1:
        return number
    tempList = [1]
    sum = 1
    k = 1
    while k < number:
        result = 1 + sum
        sum += result
        k += 1
    return result

'''
思路：设跳上第n级台阶的函数为f(x)，则青蛙可以先跳上1级台阶，再一次跳上n-1级；或者先跳上2级，再一次跳n-2级...；先跳n-1级，再一次跳上1级；直接一次跳上n级。于是f(x)=1+f(x-1)+f(x-2)+...+f(1)。
边界：
0、1、2、3
27,28（得数约为INT_MAX)
'''
# 测试用例
print('输入：%s\t输出：%s\t答案：%s' % (0, jumpFloor(0), 0))
print('输入：%s\t输出：%s\t答案：%s' % (1, jumpFloor(1), 1))
print('输入：%s\t输出：%s\t答案：%s' % (2, jumpFloor(2), 2))
print('输入：%s\t输出：%s\t答案：%s' % (3, jumpFloor(3), 4))
print('输入：%s\t输出：%s\t答案：%s' % (4, jumpFloor(4), 8))
print('输入：%s\t输出：%s\t答案：%s' % (27, jumpFloor(27), 67108864))
print('输入：%s\t输出：%s\t答案：%s' % (28, jumpFloor(28), 134217728))
