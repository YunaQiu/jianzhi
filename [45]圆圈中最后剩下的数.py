# -*- coding: utf-8 -*-
'''
n个数围成一个圈，数字分别是0~n-1。随机指定一个数m，从第一个数开始数，每次数到m时剔除该位的数字，然后接着数m个数...直至圈中只剩下最后一个数，问该数为多少。
'''

def circleRemainNum(n, m):
    if n <= 0 or m <= 0:
        return -1
    if n == 1:
        return 0
    if m == 1:
        return n-1
    numList = list(range(n))
    while len(numList) > 1:
        out = m % len(numList) - 1
        out = out if out >= 0 else out + len(numList)
        newList = [] if out == len(numList) - 1 else numList[out+1:]
        newList += [] if out == 0 else numList[:out]
        numList = newList
    return numList[0]

'''
思路：用一个序列存储当前编号，设序列长度为l，序列头部即为报数开始的位置。则第下标为m%l-1的数便是该轮被剔除的数字。将该数字之后的序列与数字前的序列拼接得到下一轮的序列。循环求解，直到序列长度为1
边界：n为0,1,2，m为0,1,2，m大于n，小于n，等于n。
注：牛客将非法值定为-1
'''
# 测试用例
print('输入：%s %s，输出：%s，答案：%s' % (1, 0, circleRemainNum(1,0), -1))
print('输入：%s %s，输出：%s，答案：%s' % (0, 1, circleRemainNum(0,1), -1))
print('输入：%s %s，输出：%s，答案：%s' % (1, 1, circleRemainNum(1,1), 0))
print('输入：%s %s，输出：%s，答案：%s' % (2, 1, circleRemainNum(2,1), 1))
print('输入：%s %s，输出：%s，答案：%s' % (2, 2, circleRemainNum(2,2), 0))
print('输入：%s %s，输出：%s，答案：%s' % (3, 3, circleRemainNum(3,3), 1))
print('输入：%s %s，输出：%s，答案：%s' % (3, 2, circleRemainNum(3,2), 2))
print('输入：%s %s，输出：%s，答案：%s' % (3, 4, circleRemainNum(3,4), 1))
print('输入：%s %s，输出：%s，答案：%s' % (5, 3, circleRemainNum(5,3), 3))
