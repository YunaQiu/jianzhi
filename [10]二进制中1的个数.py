# -*- coding: utf-8 -*-
'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
def numberOf1(n):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    while n > INT_MAX:
        n = n - INT_MAX + INT_MIN
    while n < INT_MIN:
        n = n + INT_MAX - INT_MIN
    if n==0:
        return 0
    temp = 0
    if n > 0:
        while n != 0:
            n &= n-1
            temp += 1
        return temp
    else:
        while n != -1:
            n |= n+1
            temp += 1
        return 32 - temp

'''
思路：注意整数二进制总共有32位，表示范围为:-2^31~2^31-1。而python的数值位数是动态扩充的，因此不能采用需要不断计算高位1的方案。
比如输入一个正数n，最快的思路就是不断计算n=n&(n-1)，每次与运算结束都会把二进制数字最右边的1去除，直到n为0。
对于负数n，则是不断计算n=n|(n+1)，即每次运算把最右边的0去除，直至n为-1，此时迭代次数即为0的个数，用32-迭代次数即为int表示时1的个数
边界：输入为1,0，-1，-2,INT_MAX,INT_MIN，超出INT_MAX,INT_MIN
'''
# 测试用例
print('输入：%s，输出：%s，答案，%s' % (0, numberOf1(0), 0))
print('输入：%s，输出：%s，答案，%s' % (1, numberOf1(1), 1))
print('输入：%s，输出：%s，答案，%s' % (-1, numberOf1(-1), 32))
print('输入：%s，输出：%s，答案，%s' % (-2, numberOf1(-2), 31))
print('输入：%s，输出：%s，答案，%s' % (-7, numberOf1(-7), 30))
print('输入：%s，输出：%s，答案，%s' % (7, numberOf1(7), 3))
