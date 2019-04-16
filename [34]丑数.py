# -*- coding: utf-8 -*-
'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

def uglyNumber(n):
    if n <= 1:
        return n
    uglyList = [1]
    p = {x:0 for x in [2,3,5]}
    for i in range(1,n):
        value = {k:k*uglyList[v] for k,v in p.items()}
        minV = min(value.values())
        uglyList.append(minV)
        for k,v in value.items():
            if v==minV:
                p[k] += 1
    return uglyList.pop()

'''
思路：从1开始，给因子2/3/5分别设立一个指针，初始位置指向1，并维护一个丑数列表。当求下一个丑数时，将三个指针代表值分别乘上指向的数，取最小的数作为下一个丑数，同时该指针向前挪一位。从而迭代求解出第N个丑数
注意：题目没说第0个丑数是多少
边界：n为0,1,2,3,4,大数1000
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % (0, uglyNumber(0), 0))
print('输入：%s，输出：%s，答案：%s' % (1, uglyNumber(1), 1))
print('输入：%s，输出：%s，答案：%s' % (2, uglyNumber(2), 2))
print('输入：%s，输出：%s，答案：%s' % (3, uglyNumber(3), 3))
print('输入：%s，输出：%s，答案：%s' % (4, uglyNumber(4), 4))
print('输入：%s，输出：%s，答案：%s' % (5, uglyNumber(5), 5))
print('输入：%s，输出：%s，答案：%s' % (7, uglyNumber(7), 8))
print('输入：%s，输出：%s，答案：%s' % (10, uglyNumber(10), 12))
print('输入：%s，输出：%s，答案：%s' % (1000, uglyNumber(1000), '?'))
