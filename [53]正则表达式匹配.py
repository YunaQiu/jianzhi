# -*- coding: utf-8 -*-
'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''

def matchReg(string, pattern):
    if len(pattern) == 0:
        return True if len(string) == 0 else False
    si = pi = 0
    while pi < len(pattern):
        if si == len(string):
            if pi == len(pattern)-1 or pattern[pi+1] != '*':
                return False
            pi += 2
            continue

        if pi == len(pattern) - 1 or pattern[pi+1] != '*':
            if pattern[pi] != '.' and string[si] != pattern[pi]:
                return False
            si += 1
            pi += 1
        elif pattern[pi] != '.' and string[si] != pattern[pi]:
            pi += 2
        else:
            return matchReg(string[si:], pattern[pi+2:]) or matchReg(string[si+1:], pattern[pi+2:]) or matchReg(string[si+1:], pattern[pi:])
    return (si == len(string) and pi == len(pattern))

'''
思路：这题的难点主要在*的判断上。当字符a碰到能够匹配的*（比如a*或者.*）时，其实有三种暗含的情况：一种是一次都不匹配一种是只匹配一次，一种是会匹配多次。如果考虑递归，第一种情况就是匹配包括a的后面的字符跟*后面的模式是否匹配；第二种情况是匹配a之后的字符跟*后面的模式是否匹配；第三种情况是匹配a之后的字符跟a*以及后面的模式是否匹配。只要一种成功即可
边界：字符串为空，模式为空，字符串为空且模式为'x*'，模式不带.跟*，模式有.，模式有*且可匹配不止一次，模式有.*。
'''
# 测试用例
print('输入：%s %s，输出：%s，答案：%s' % ('','', matchReg('',''), True))
print('输入：%s %s，输出：%s，答案：%s' % ('','a', matchReg('','a'), False))
print('输入：%s %s，输出：%s，答案：%s' % ('','a*', matchReg('','a*'), True))
print('输入：%s %s，输出：%s，答案：%s' % ('','a*b*', matchReg('','a*b*'), True))
print('输入：%s %s，输出：%s，答案：%s' % ('ab','', matchReg('ab',''), False))
print('输入：%s %s，输出：%s，答案：%s' % ('ab','ab', matchReg('ab','ab'), True))
print('输入：%s %s，输出：%s，答案：%s' % ('abb','a.b', matchReg('abb','a.b'), True))
print('输入：%s %s，输出：%s，答案：%s' % ('abb','ab*', matchReg('abb','ab*'), True))
print('输入：%s %s，输出：%s，答案：%s' % ('abbc','ab*', matchReg('abbc','ab*'), False))
print('输入：%s %s，输出：%s，答案：%s' % ('ac','ab*c', matchReg('ac','ab*c'),True))
print('输入：%s %s，输出：%s，答案：%s' % ('abc','a.*c', matchReg('abc','a.*c'),True))
print('输入：%s %s，输出：%s，答案：%s' % ('abcccca','a.*ca', matchReg('abcccca','a.*ca'),True))
print('输入：%s %s，输出：%s，答案：%s' % ('abcccca','a.*ab', matchReg('abcccca','a.*ab'),False))
print('输入：%s %s，输出：%s，答案：%s' % ('abccccac','a.*ab', matchReg('abccccac','a.*ab'),False))
