# -*- coding: utf-8 -*-
'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
'''

class CharStreaming:
    def __init__(self):
        self.hashList = [0] * 256
        self.firstQue = []

    def add(self, c):
        for x in c:
            cOrd = ord(c)
            if self.hashList[cOrd] == 0:
                self.hashList[cOrd] = 1
                self.firstQue.append(x)
            else:
                self.hashList[cOrd] = 2
        while len(self.firstQue) > 0:
            cOrd = ord(self.firstQue[0])
            if self.hashList[cOrd] > 1:
                self.firstQue.pop(0)
            else:
                break

    def first(self):
        if len(self.firstQue) > 0:
            return self.firstQue[0]
        else:
            return '#'

'''
思路：用一个hash表存储256种字符出现的次数，并用一个队列存储可能的第一个唯一字符。当添加一个字符时，若字符未出现过，则次数记1同时加入到队列末尾；若字符出现过，则次数记2，同时循环判断队头是否满足唯一条件，不满足则弹出。获取第一个只出现一次的字符，其实就是获取队头，若队列为空，返回#
其他思路：如果用hash表存储第一个字符出现的位置，则可以节省掉队列空间。不过在查找第一个字符的字符的时候就需要对哈希表遍历。
边界：空字符流，连续不重复字符，有重复字符且是队头，有重复字符但不是队头，队头包含连续多个重复字符。空队列
'''
# 测试用例
charS = CharStreaming()
print('输入：%s，输出：%s，答案：%s' % ('', charS.first(), '#'))
charS.add('a')
print('输入：%s，输出：%s，答案：%s' % ('a', charS.first(), 'a'))
charS.add('b')
charS.add('c')
print('输入：%s，输出：%s，答案：%s' % ('bc', charS.first(), 'a'))
charS.add('b')
print('输入：%s，输出：%s，答案：%s' % ('b', charS.first(), 'a'))
charS.add('a')
print('输入：%s，输出：%s，答案：%s' % ('a', charS.first(), 'c'))
charS.add('c')
print('输入：%s，输出：%s，答案：%s' % ('c', charS.first(), '#'))
