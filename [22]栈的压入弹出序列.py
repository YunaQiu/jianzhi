# -*- coding: utf-8 -*-
'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''
def isPopOrder(pushL, popL):
    if len(pushL)==0:
        return True
    stack = []
    inI = 0
    for x in popL:
        while len(stack)==0 or stack[-1]!= x:
            if inI >= len(pushL):
                return False
            stack.append(pushL[inI])
            inI += 1
        stack.pop()
    return True

'''
思路：建一个栈模拟操作。遍历读取出栈顺序，如读到元素k，若栈顶是k，则直接弹出。若栈顶不是k，则从入栈顺序中依次压入，直到碰到k后将其弹出。若入栈压完后依然不能完成所有出栈操作，则返回false，否则返回true
边界：两个空序列，只有1个值，有2个值，多个值且为true，多个值且为false
'''
# 测试用例
print('输入：%s %s，输出：%s，答案：%s' % ([], [], isPopOrder([], []), True))
print('输入：%s %s，输出：%s，答案：%s' % ([1], [1], isPopOrder([1], [1]), True))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2], [1,2], isPopOrder([1,2], [1,2]), True))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2], [2,1], isPopOrder([1,2], [2,1]), True))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2,3,4], [3,2,4,1], isPopOrder([1,2,3,4], [3,2,4,1]), True))
print('输入：%s %s，输出：%s，答案：%s' % ([1,2,3,4], [2,4,1,3], isPopOrder([1,2,3,4], [2,4,1,3]), False))
