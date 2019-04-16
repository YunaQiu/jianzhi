# -*- coding: utf-8 -*-
'''
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
'''

def reverseSentence(sentence):
    if len(sentence) <= 1:
        return sentence
    sentence = list(sentence)
    reverseCore(sentence, 0, len(sentence)-1)
    head = tail = 0
    while head < len(sentence)-1:
        if sentence[head] == ' ':
            head = tail = head + 1
        elif tail == len(sentence) or sentence[tail] == ' ':
            reverseCore(sentence, head, tail-1)
            head = tail = tail + 1
        else:
            tail += 1
    return ''.join(sentence)

def reverseCore(strList, start, end):
    if start == end:
        return
    while start < end:
        strList[start], strList[end] = strList[end], strList[start]
        start += 1
        end -= 1

'''
思路：先翻转所有字符：从两端向中间逐渐调转字符，同时记录下所有空格位，再翻转其中的单词字符。
边界：空句子，只有一个单词，只有1个字符，只有空格，有奇数字符，有偶数字符，有多个单词，有多个空格。
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % ('', reverseSentence(''), ''))
print('输入：%s，输出：%s，答案：%s' % ('I', reverseSentence('I'), 'I'))
print('输入：%s，输出：%s，答案：%s' % (' ', reverseSentence(' '), ' '))
print('输入：%s，输出：%s，答案：%s' % ('am', reverseSentence('am'), 'am'))
print('输入：%s，输出：%s，答案：%s' % ('cat', reverseSentence('cat'), 'cat'))
print('输入：%s，输出：%s，答案：%s' % ('cat fish.', reverseSentence('cat fish.'), 'fish. cat'))
print('输入：%s，输出：%s，答案：%s' % ('cat eat fish', reverseSentence('cat eat fish'), 'fish eat cat'))
print('输入：%s，输出：%s，答案：%s' % ('cat eat fish before.', reverseSentence('cat eat fish before.'), 'before. fish eat cat'))
print('输入：%s，输出：%s，答案：%s' % ('I cat eat fish before.', reverseSentence('I cat eat fish before.'), 'before. fish eat cat I'))
print('输入：%s，输出：%s，答案：%s' % ('cat  eat fish   before .', reverseSentence('cat  eat fish   before .'), '. before   fish eat  cat'))
