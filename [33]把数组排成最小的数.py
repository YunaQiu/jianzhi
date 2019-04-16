# -*- coding: utf-8 -*-
'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
from functools import cmp_to_key
def printMin(numList):
    def customCmp(x1, x2):
        x1,x2 = str(x1),str(x2)
        h1,h2 = int(x1+x2),int(x2+x1)
        if h1 == h2:
            return 0
        elif h1 < h2:
            return -1
        else:
            return 1
    if len(numList) == 0:
        return ''
    if len(numList) == 1:
        return str(numList[0])
    numList = sorted(numList, key=cmp_to_key(customCmp))
    result = []
    [result.append(str(x)) for x in numList]
    return ''.join(result)

'''
思路：其实就是定义排序规则，再把排序后的数拼接起来。排序方案类似于字典序，但与字典序有所不同（21>211）。具体来说其实就是比较两个数拼接后哪个数更小，从而确定两个数的大小顺序。因此需要数学论证是否满足偏序定义（即自反性、对称性、传递性）
注：题目没说返回值是int还是str,也没说空数组应该返回什么
边界：空数组，只有一个数，开头数字相同，多个相同数字
'''
print('输入：%s，输出：%s，答案：%s' % ([], printMin([]), ''))
print('输入：%s，输出：%s，答案：%s' % ([23], printMin([23]), 23))
print('输入：%s，输出：%s，答案：%s' % ([23,51,2], printMin([23,51,2]), 22351))
print('输入：%s，输出：%s，答案：%s' % ([21,51,211,21], printMin([21,51,211,21]), 211212151))
