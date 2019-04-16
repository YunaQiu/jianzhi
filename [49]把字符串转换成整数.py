# -*- coding: utf-8 -*-
'''
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
'''

def covertNum(numStr):
    numStr = list(numStr.strip())
    sgn = 1
    intPart = 0

    if len(numStr) == 0:
        return 0
    sgn = -1 if numStr[0] == '-' else 1
    numStr = numStr[1:] if numStr[0]=='+' or numStr[0]=='-' else numStr

    while len(numStr)>0:
        x = numStr[0]
        if x < '0' or x > '9':
            return 0
        intPart = intPart*10 + ord(x) - ord('0')
        numStr.pop(0)

    return intPart*sgn


'''
思路：合法的整数可能包括正负号，允许两端空格。因此要先去空格，然后记录可能的符号位，整数部分从高位逐位乘10相加。（如果还要考虑浮点数的整数部分，要考虑科学计数法，那恐怕要爆炸了）
边界：空字符串，带前/后空格，中间有空格，前面有多个0，有符号，有其他字符
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % ('', covertNum(''), 0))
print('输入：%s，输出：%s，答案：%s' % (' A', covertNum(' A'), 0))
print('输入：%s，输出：%s，答案：%s' % (' 1 ', covertNum(' 1 '), 1))
print('输入：%s，输出：%s，答案：%s' % (' 021', covertNum(' 021'), 21))
print('输入：%s，输出：%s，答案：%s' % (' +021', covertNum(' +021'), 21))
print('输入：%s，输出：%s，答案：%s' % (' -021', covertNum(' -021'), -21))
print('输入：%s，输出：%s，答案：%s' % (' -02 1', covertNum(' -02 1'), 0))
print('输入：%s，输出：%s，答案：%s' % (' -020.0', covertNum(' -020.0'), 0))
print('输入：%s，输出：%s，答案：%s' % (' -020.01', covertNum(' -020.01'), 0))
