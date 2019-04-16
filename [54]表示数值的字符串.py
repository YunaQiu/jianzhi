# -*- coding: utf-8 -*-
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''

def isNumeric(s):
    s = s.strip()
    part = 'num'
    hasDigit = False
    for i in range(len(s)):
        if s[i].isdigit():
            hasDigit = True
        elif s[i] == '.':
            if part != 'num':
                return False
            part = 'frac'
        elif s[i].lower() == 'e':
            if part == 'e' or not hasDigit:
                return False
            part = 'e'
            hasDigit = False
        elif s[i] == '+' or s[i] == '-':
            if i != 0 and s[i-1].lower() != 'e':
                return False
        else:
            return False
    return hasDigit

'''
思路：合法的数值应该是满足[sign]digit[.[digit]][E|e[sign]digit]或者[sign][digit].digit[E|e[sign]digit]，且还允许字符串有两端空格，情况比较复杂，因此可以直接考虑特殊字符的情况：去两端空格后，正负号只能出现在第一位或者e|E的后一位；小数点只能出现一次且前面不能有e|E；e|E只能出现1次且前后都必须是合法数值。可以根据小数点和E把数值分为整数部分、小数部分和指数部分，整数部分跟小数部分至少一个有值，指数部分必须有值。
边界：空字符串，两端空白，中间空白，无符号数，有正负号数，有多个正负号，只有正负号，有多个小数点，小数点后无数字，小数点前无数字，有多个e，e后面有无正负号，e后面有无小数点......
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % (' ', isNumeric(' '), False))
print('输入：%s，输出：%s，答案：%s' % (' -', isNumeric(' -'), False))
print('输入：%s，输出：%s，答案：%s' % (' -.', isNumeric(' -.'), False))
print('输入：%s，输出：%s，答案：%s' % (' -.e', isNumeric(' -.e'), False))
print('输入：%s，输出：%s，答案：%s' % (' -.5', isNumeric(' -.5'), True))
print('输入：%s，输出：%s，答案：%s' % (' 24', isNumeric(' 24'), True))
print('输入：%s，输出：%s，答案：%s' % (' 24a', isNumeric(' 24a'), False))
print('输入：%s，输出：%s，答案：%s' % (' 2 4', isNumeric(' 2 4'), False))
print('输入：%s，输出：%s，答案：%s' % (' +24', isNumeric(' +24'), True))
print('输入：%s，输出：%s，答案：%s' % ('+-24', isNumeric('+-24'), False))
print('输入：%s，输出：%s，答案：%s' % ('-24.', isNumeric('-24.'), True))
print('输入：%s，输出：%s，答案：%s' % ('-24.50', isNumeric('-24.50'), True))
print('输入：%s，输出：%s，答案：%s' % ('-24.50e', isNumeric('-24.50e'), False))
print('输入：%s，输出：%s，答案：%s' % ('-e3', isNumeric('-e3'), False))
print('输入：%s，输出：%s，答案：%s' % ('-12.e3', isNumeric('-12.e3'), True))
print('输入：%s，输出：%s，答案：%s' % ('-24.50e4', isNumeric('-24.50e4'), True))
print('输入：%s，输出：%s，答案：%s' % ('-24.50E4', isNumeric('-24.50E4'), True))
print('输入：%s，输出：%s，答案：%s' % ('-24.50E+4', isNumeric('-24.50E+4'), True))
print('输入：%s，输出：%s，答案：%s' % ('-24.50E+4.5', isNumeric('-24.50E+4.5'), False))
