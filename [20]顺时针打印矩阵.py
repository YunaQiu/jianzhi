# -*- coding: utf-8 -*-
'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
备注：牛客网上要求不打印，直接返回列表
'''
def printMatrix(matrix):
    if matrix is None or len(matrix)==0 or len(matrix[0])==0:
        return []
    strList = []
    printCore(matrix, strList, 0, len(matrix)-1, 0, len(matrix[0])-1)
    # [print('%s'%x, end=',') for x in strList[:-1]]
    # print('%s.' % strList[-1])
    return strList

def printCore(matrix, out, startRow, endRow, startCol, endCol):
    if startRow == endRow:
        out.extend([matrix[startRow][i] for i in range(startCol,endCol+1)])
        return
    if startCol == endCol:
        out.extend([matrix[i][startCol] for i in range(startRow,endRow+1)])
        return
    out.extend([matrix[startRow][i] for i in range(startCol,endCol)])
    out.extend([matrix[i][endCol] for i in range(startRow,endRow)])
    out.extend([matrix[endRow][i] for i in range(endCol,startCol,-1)])
    out.extend([matrix[i][startCol] for i in range(endRow, startRow, -1)])
    if endRow-startRow>1 and endCol-startCol>1:
        printCore(matrix, out, startRow+1, endRow-1, startCol+1, endCol-1)

'''
思路：指定矩阵的开始行、结束行、开始列、结束列，每次按开始行=》结束列=》结束行倒序=》开始列倒序的顺序打印，每次打印时包头不包尾，逐层向内遍历。
对于单行或单列的特殊情况，则必然是从上到下打印或从左到右打印
边界：空矩阵(None,[],[[]])，只有一个元素，单行矩阵，单列矩阵，两行矩阵，两列矩阵，偶数行偶数列矩阵，单数行的宽矩阵，单数列的长矩阵
'''
# 测试用例
print('输入：%s\n输出：' % None, end='')
printMatrix(None)
print('\n输入：%s\n输出：' % [], end='')
printMatrix([])
print('\n输入：%s\n输出：' % [[]], end='')
printMatrix([[]])
print('\n输入：%s\n输出：' % [[1]], end='')
printMatrix([[1]])
matrix = [[1,2,3,4]]
print('输入：%s\n输出：' % matrix, end='')
printMatrix(matrix)
matrix = [[1],[2],[3],[4]]
print('输入：%s\n输出：' % matrix, end='')
printMatrix(matrix)
matrix = [
    [1,2,3,4],
    [5,6,7,8]
]
print('输入：%s\n输出：' % matrix, end='')
printMatrix(matrix)
matrix = [
    [1,2],
    [3,4],
    [5,6],
    [7,8]
]
print('输入：%s\n输出：' % matrix, end='')
printMatrix(matrix)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
print('输入：%s\n输出：' % matrix, end='')
printMatrix(matrix)
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print('输入：%s\n输出：' % matrix, end='')
printMatrix(matrix)
