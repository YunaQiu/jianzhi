# -*- coding: utf-8 -*-
'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
'''

def firstUnique(string):
    if len(string) == 0:
        return -1
    if len(string) == 1:
        return 0
    hashList = [-1] * 128
    for i,x in enumerate(string):
        key = ord(x)
        if hashList[key] == -1:
            hashList[key] = i
        else:
            hashList[key] = -2
    first = -1
    for x in hashList:
        if x >= 0:
            first = x if first == -1 else min(first, x)
    return first

'''
思路：字符串只由字母组成，因此总共有52种可能字符。可以根据ASCII码建一个长度128的哈希表存放字符状态。用-1表示未出现，0及以上表示第一次出现的位置，-2表示出现多次。则总共只需要遍历一次字符串，再遍历一次哈希表即可求得。
边界：字符串长度为0/1/10000，全部是重复字符，有多个只出现一次的字符
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % ('', firstUnique(''), -1))
print('输入：%s，输出：%s，答案：%s' % ('v', firstUnique('v'), 0))
print('输入：%s，输出：%s，答案：%s' % ('vv', firstUnique('vv'), -1))
print('输入：%s，输出：%s，答案：%s' % ('vvkb', firstUnique('vvkb'), 2))
print('输入：%s，输出：%s，答案：%s' % ('abcde*2000', firstUnique('abcde'*2000), -1))
