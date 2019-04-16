# -*- coding: utf-8 -*-
'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
注意：牛客的测试用例中，矩阵的输入格式为字符串+行数+列数，而不是二维矩阵
'''

def pathInMatrix(matrix, rows, cols, path):
    if rows <= 0 or cols <= 0 or len(matrix) != rows*cols:
        return False
    matrix = [[matrix[i*cols+j] for j in range(cols)] for i in range(rows)]
    if path == '':
        return True
    mask = [[False] * cols for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == path[0] and stepMatrix(matrix, mask, path[1:], i, j):
                return True
    return False

def stepMatrix(matrix, mask, path, i, j):
    mask[i][j] = True
    if path == '':
        return True
    for x,y in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
        if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and not(mask[x][y]) and matrix[x][y] == path[0]:
            if stepMatrix(matrix, mask, path[1:], x, y):
                return True
    mask[i][j] = False
    return False

'''
思路：新建一个同等大小的矩阵记录已走过的路程。采用递归求解，若有下一步能走，则记录下已走过的点，然后将剩余路径传入下一层递归中。
边界：矩阵为空，路径为空，重复格子可行但不重复不可行。斜对角不可行。有多条路径。
'''
# 测试用例
print('输入：%s %s %s %s，输出：%s，答案：%s' % ('',0,0,'qew', pathInMatrix('',0,0,'qew'), False))
print('输入：%s %s %s %s，输出：%s，答案：%s' % ('w',1,1,'', pathInMatrix('w',1,1,''), True))
print('输入：%s %s %s %s，输出：%s，答案：%s' % ('abcd',2,2,'ad', pathInMatrix('abcd',2,2,'ad'), False))
print('输入：%s %s %s %s，输出：%s，答案：%s' % ('abcd',2,2,'ac', pathInMatrix('abcd',2,2,'ac'), True))
print('输入：%s %s %s %s，输出：%s，答案：%s' % ('abcd',2,2,'abcda', pathInMatrix('abcd',2,2,'abcda'), False))
print('输入：%s %s %s %s，输出：%s，答案：%s' % ('abcdad',3,2,'acdba', pathInMatrix('abcdad',3,2,'acdba'), True))
