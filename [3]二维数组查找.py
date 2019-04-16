# -*- coding: utf-8 -*-

'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

def find(matrix, num):
    if len(matrix) == 0:
        return False
    elif len(matrix[0]) == 0:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    i = 0
    j = cols - 1

    while (i < rows) and (j >= 0):
        temp = matrix[i][j]
        if temp == num:
            return True
        if temp < num:
            i += 1
        else:
            j -= 1
    return False


'''
思路：从右上角开始，比当前数字大说明在当前行下方，比当前数字小说明在当前列的左边
测试用例：
输入空数组，只有一个元素的二维数组
数字在左上角/右上角/左下角/右下角/
数字不在数组中（比任何数字大，比任何数字小，中间取值）
'''
# 测试用例
print('输入:%s %d，输出：%s，答案：%s' % ([[]], 3, find([[]], 3), False))
print('输入:%s %d，输出：%s，答案：%s' % ([[1]], 3, find([[1]], 3), False))
print('输入:%s %d，输出：%s，答案：%s' % ([[0]], 0, find([[0]], 0), True))
matrix = [
    [2,3,6,8,9],
    [4,7,11,12,15],
    [5,10,16,26,27],
    [13,17,20,28,30]
]
print('输入:%s %d，输出：%s，答案：%s' % (matrix, 2, find(matrix, 2), True))
print('输入:%s %d，输出：%s，答案：%s' % (matrix, 9, find(matrix, 9), True))
print('输入:%s %d，输出：%s，答案：%s' % (matrix, 13, find(matrix, 13), True))
print('输入:%s %d，输出：%s，答案：%s' % (matrix, 30, find(matrix, 30), True))
print('输入:%s %d，输出：%s，答案：%s' % (matrix, 1, find(matrix, 1), False))
print('输入:%s %d，输出：%s，答案：%s' % (matrix, 32, find(matrix, 32), False))
print('输入:%s %d，输出：%s，答案：%s' % (matrix, 18, find(matrix, 18), False))
