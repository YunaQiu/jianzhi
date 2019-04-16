# -*- coding: utf-8 -*-
'''
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
'''

def rotateLeft(s, k):
    if len(s) == 0:
        return []
    k %= len(s)
    if k == 0:
        return s
    # 注意：python不支持修改字符串常量
    s = list(s)
    return ''.join(rotatePart(s, 0, k))

def rotatePart(s, start, k):
    p1,p2 = start, start+k
    while p2 < len(s):
        s[p1], s[p2] = s[p2], s[p1]
        p1 += 1
        p2 += 1
    remain = (len(s)-start) % k
    return s if remain == 0 else rotatePart(s, len(s)-k, k-remain)

'''
思路：两个间隔为k位的指针，以k为一周期从左往右移动，每次移动都调换两个指针的字符。当移动到末尾时若不满一个周期，则递归旋转剩余部分和已旋转部分的字符串。
边界：只有0/1/2个字符，左移位数为0，左移位数等于长度，左移位数大于长度，正好满周期，末尾剩余1,2个字符
'''
print('输入：%s %s，' % ("", 1), '输出：%s，答案：%s' % (rotateLeft("",1), ""))
print('输入：%s %s，' % ("1", 1), '输出：%s，答案：%s' % (rotateLeft("1",1), "1"))
print('输入：%s %s，' % ("12", 1), '输出：%s，答案：%s' % (rotateLeft("12",1), "21"))
print('输入：%s %s，' % ("12", 0), '输出：%s，答案：%s' % (rotateLeft("12",0), "12"))
print('输入：%s %s，' % ("12", 2), '输出：%s，答案：%s' % (rotateLeft("12",2), "12"))
print('输入：%s %s，' % ("12", 3), '输出：%s，答案：%s' % (rotateLeft("12",3), "21"))
print('输入：%s %s，' % ("1234", 2), '输出：%s，答案：%s' % (rotateLeft("1234",2), "3412"))
print('输入：%s %s，' % ("1234", 3), '输出：%s，答案：%s' % (rotateLeft("1234",3), "4123"))
print('输入：%s %s，' % ("12345", 3), '输出：%s，答案：%s' % (rotateLeft("12345",3), "45123"))
