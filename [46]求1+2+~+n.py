# -*- coding: utf-8 -*-
'''
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

def cumSum(n):
    def nonZero(n):
        return n + cumSum(n-1)
    def isZero(n):
        return 0
    judge = {False: isZero, True: nonZero}
    return judge[bool(n)](n)

'''
思路：循环用递归代替，结束条件改为用字典控制。数字可以用bool转成二元。则最基础的方案是对n求bool，若是True则返回0，若是False则返回n+sum(n-1)。(该方案已能通过牛客检验)
边界：n为0,1,2,100
'''
# 测试用例
print('输入：%s，输出：%s，答案：%s' % (0, cumSum(0), 0))
print('输入：%s，输出：%s，答案：%s' % (1, cumSum(1), 1))
print('输入：%s，输出：%s，答案：%s' % (2, cumSum(2), 3))
print('输入：%s，输出：%s，答案：%s' % (3, cumSum(3), 6))
print('输入：%s，输出：%s，答案：%s' % (100, cumSum(100), 5050))
