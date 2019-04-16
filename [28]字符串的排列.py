# -*- coding: utf-8 -*-
'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
注：牛客网是要求返回结果数组
'''
def permutation(ss):
    ss = list(ss)
    ss.sort()
    rsList = []
    core(ss, '', rsList)
    return rsList

def core(slist, head, rsList):
    if len(slist) == 1:
        # print(head + slist[0])
        rsList.append(head + slist[0])
        return
    for i in range(len(slist)):
        if i>0 and slist[i] == slist[i-1]:
            continue
        temp = slist.copy()
        temp.pop(i)
        core(temp, head + slist[i], rsList)

'''
思路：对字符串排序后，先固定第一个字符，然后递归求解后面的字符。
边界：空字符串，只有一个字符，全部字符相同，多个字符相同，全部不相同，长度为9且不相同(长数组建议丢网上测)
'''
print('输入：%s, 输出：%s' % ('', permutation('')))
print('输入：%s, 输出：%s' % ('a', permutation('a')))
print('输入：%s, 输出：%s' % ('aaaa', permutation('aaaa')))
print('输入：%s, 输出：%s' % ('bcad', permutation('bcad')))
print('输入：%s, 输出：%s' % ('abbd', permutation('abbd')))
# print('输入：%s, 输出：%s' % ('abcdefghij', permutation('abcdefghij')))
