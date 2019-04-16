# -*- coding: utf-8 -*-
'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

def power(base, exponent):
    if exponent == 0:
        return 1
    frac = (exponent < 0)
    if abs(exponent) == 1:
        return (1/base) if frac else base
    elif exponent % 2 == 0:
        temp = power(base, exponent/2)
        return temp * temp
    else:
        temp = power(base, (exponent-1)/2)
        return temp * temp * base

'''
思路：0次方统一返回1（0的0次方无定义），负数次方为先求整数次方，再用1除。
因为是整数次方，可以一个个数乘上去，但效率太低，因此考虑套用公式：
x^a = x^(a/2) * x^(a/2)             //a为偶数时
x^a = x^(a-1/2) * x^(a-1/2) * x     //a为奇数时
边界：0^0,1^0,2^0,2^-1,2^-2,2^2,-2^31,-2^30
'''
# 测试用例
print('输入：%s，%s\t输出：%s\t答案：%s' % (0, 0, power(0,0), 1))
print('输入：%s，%s\t输出：%s\t答案：%s' % (1, 0, power(1,0), 1))
print('输入：%s，%s\t输出：%s\t答案：%s' % (2, 0, power(2,0), 1))
print('输入：%s，%s\t输出：%s\t答案：%s' % (2, -1, power(2,-1), 2**(-1)))
print('输入：%s，%s\t输出：%s\t答案：%s' % (2, -2, power(2,-2), 2**(-2)))
print('输入：%s，%s\t输出：%s\t答案：%s' % (2, 2, power(2,2), 2**2))
print('输入：%s，%s\t输出：%s\t答案：%s' % (-2, 2, power(-2,2), (-2)**2))
print('输入：%s，%s\t输出：%s\t答案：%s' % (-2, 30, power(-2,30), (-2)**30))
print('输入：%s，%s\t输出：%s\t答案：%s' % (-2, 31, power(-2,31), (-2)**31))
