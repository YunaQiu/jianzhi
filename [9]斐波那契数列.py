# -*- coding: utf-8 -*-

'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    x1, x2, i, f = 0, 1, 2, 1
    while i <= n:
        f = x1 + x2
        x1 = x2
        x2 = f
        i += 1
    return f

'''
思路：斐波那契数列公式为f(n)=f(n-1)+f(n-2)，若用递归来写，例如f(k)=f(k-1)+f(k-2)=2f(k-2)+f(k-3)，则递归深度太深，且每个值都计算了两次。其实只需要记录最近的两个迭代值就可以了，改用循环实现。
边界：
0,1,2,3
38,39
'''
print('输入：%s\t输出：%s\t答案：%s' % (0, fibonacci(0), 0))
print('输入：%s\t输出：%s\t答案：%s' % (1, fibonacci(1), 1))
print('输入：%s\t输出：%s\t答案：%s' % (2, fibonacci(2), 1))
print('输入：%s\t输出：%s\t答案：%s' % (3, fibonacci(3), 2))
print('输入：%s\t输出：%s\t答案：%s' % (38, fibonacci(38), 39088169))
print('输入：%s\t输出：%s\t答案：%s' % (39, fibonacci(39), 63245986))
