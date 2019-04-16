# -*- coding: utf-8 -*-
'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
牛客要求：找到任意重复的一个值并赋值到duplication[0]，函数返回True/False
'''

def repeatNum(numList, dup):
    if len(numList) <= 1:
        return False
    i = 0
    while i < len(numList):
        if numList[i] == i:
            i += 1
        elif numList[i] == numList[numList[i]]:
            dup[0] = numList[i]
            return True
        else:
            numList[numList[i]],numList[i] = numList[i], numList[numList[i]]
    return False

'''
思路：因为范围在0~n-1之间，所以可以用一个长度n的hash保存，遍历数组，若数字在哈希表中，则返回该数字。
思路2：依次将数字放到对应的下标位置，若有重复数字，比如有两个数字下标相同。
边界：空数组，只有一个数字，全部不重复，全部相同，只有一个重复，有多个重复
'''
# 测试用例
dup = [None]
print('输入：%s，输出：%s %s，答案：%s' % ([], repeatNum([],dup), dup, False))
print('输入：%s，输出：%s %s，答案：%s' % ([1], repeatNum([1],dup), dup, False))
print('输入：%s，输出：%s %s，答案：%s' % ([1,0,2], repeatNum([1,0,2],dup), dup, False))
print('输入：%s，输出：%s %s，答案：%s' % ([1,3,0,1], repeatNum([1,3,0,1],dup), dup, 1))
print('输入：%s，输出：%s %s，答案：%s' % ([1,3,0,1,0], repeatNum([1,3,0,1,0],dup), dup, '1or0'))
print('输入：%s，输出：%s %s，答案：%s' % ([3,3,3,3], repeatNum([3,3,3,3],dup), dup, 3))
