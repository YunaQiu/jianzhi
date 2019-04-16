# -*- coding: utf-8 -*-

'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

def rectCover(number):
    if number <= 2:
        return number
    i,j,k,result = 1,2,2,2
    while k < number:
        result = i + j
        i = j
        j = result
        k += 1
    return result

'''
思路：覆盖2*n的矩形，可以先覆盖2*n-1的矩形，然后再用一个竖的矩形覆盖；也可以先覆盖2*n-2的矩形，再用两个横的矩形覆盖。于是f(x)=f(x-1)+f(x-2)，是斐波那契数列。
边界：
0、1、2、3
38/39/40（得数约为INT_MAX)
'''
# 测试用例
print('输入：%s\t输出：%s\t答案：%s' % (0, rectCover(0), 0))
print('输入：%s\t输出：%s\t答案：%s' % (1, rectCover(1), 1))
print('输入：%s\t输出：%s\t答案：%s' % (2, rectCover(2), 2))
print('输入：%s\t输出：%s\t答案：%s' % (3, rectCover(3), 3))
print('输入：%s\t输出：%s\t答案：%s' % (38, rectCover(38), 63245986))
print('输入：%s\t输出：%s\t答案：%s' % (39, rectCover(39), 102334155))
print('输入：%s\t输出：%s\t答案：%s' % (40, rectCover(40), 165580141))
