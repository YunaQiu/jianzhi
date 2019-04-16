# -*- coding: utf-8 -*-
'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''

def stepRange(m, n, k, idxI=0, idxJ=0, cover=None):
    cover = [[False]*n for i in range(m)] if cover is None else cover
    if idxI >= m or idxJ >= n or idxI < 0 or idxJ < 0 or cover[idxI][idxJ] or bitSum(idxI) + bitSum(idxJ) > k:
        return 0
    coverSize = 1
    cover[idxI][idxJ] = True
    coverSize += stepRange(m, n, k, idxI, idxJ+1, cover)
    coverSize += stepRange(m, n, k, idxI+1, idxJ, cover)
    coverSize += stepRange(m, n, k, idxI, idxJ-1, cover)
    coverSize += stepRange(m, n, k, idxI-1, idxJ, cover)
    return coverSize

def bitSum(num):
    res = 0
    while num > 0:
        res += num % 10
        num //= 10
    return res

'''
思路：对于某一点i，考虑它前后左右的格子，一步步递归遍历。（有没人能证一下是否可以省略向左走跟向上走？）
边界：m，n小于1，k小于1，k小于0，k为8,9,10，横向/纵向可抵达距离超过格子边界，某一行能抵达的格子出现分段，某一行能抵达的最远格子超过它的上一行
'''
print('输入：%s %s %s，输出：%s，答案：%s' % (0,1,3, stepRange(0,1,3), 0))
print('输入：%s %s %s，输出：%s，答案：%s' % (4,0,3, stepRange(4,0,3), 0))
print('输入：%s %s %s，输出：%s，答案：%s' % (4,1,-1, stepRange(4,1,-1), 0))
print('输入：%s %s %s，输出：%s，答案：%s' % (4,1,0, stepRange(4,1,0), 1))
print('输入：%s %s %s，输出：%s，答案：%s' % (4,1,1, stepRange(4,1,1), 2))
print('输入：%s %s %s，输出：%s，答案：%s' % (5,3,3, stepRange(5,3,3), 9))
print('输入：%s %s %s，输出：%s，答案：%s' % (3,5,3, stepRange(3,5,3), 9))
print('输入：%s %s %s，输出：%s，答案：%s' % (20,20,8, stepRange(20,20,8), 45))
print('输入：%s %s %s，输出：%s，答案：%s' % (20,20,9, stepRange(20,20,9), 145))
print('输入：%s %s %s，输出：%s，答案：%s' % (15,20,9, stepRange(15,20,9), 135))
print('输入：%s %s %s，输出：%s，答案：%s' % (20,20,10, stepRange(20,20,10), 219))
