# -*- coding: utf-8 -*-
'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''
class Stack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)
        self.s2.append(x if len(self.s2)==0 or x<=self.s2[-1] else self.s2[-1])

    def pop(self):
        if len(self.s1) != 0:
            self.s2.pop()
            return self.s1.pop()

    def min(self):
        return None if len(self.s2)==0 else self.s2[-1]

    def __str__(self):
        return str(self.s1)

'''
思路: 增加一个辅助栈，每当主栈压入一个数值时，辅助栈同时压入当前栈中的最小值（若新数比原辅助栈顶数字小，则压入新数，否则重复压入原栈顶数字），每当主栈弹出一个数值时，辅助栈也弹出栈顶。则min函数实际读取的是辅助栈的栈顶元素
边界：空栈，一个值，压入的值比原最小值小，压入的值比最小值大，弹出最小值，弹出非最小值
'''
# 测试用例
stack = Stack()
print('操作：%s，返回值：%s，' % ('pop',stack.pop()), '当前栈：%s，最小值：%s' % (stack, stack.min()))
print('操作：%s，返回值：%s，' % ('push(3)',stack.push(3)), '当前栈：%s，最小值：%s' % (stack, stack.min()))
print('操作：%s，返回值：%s，' % ('push(4)',stack.push(4)), '当前栈：%s，最小值：%s' % (stack, stack.min()))
print('操作：%s，返回值：%s，' % ('push(1)',stack.push(1)), '当前栈：%s，最小值：%s' % (stack, stack.min()))
print('操作：%s，返回值：%s，' % ('pop',stack.pop()), '当前栈：%s，最小值：%s' % (stack, stack.min()))
print('操作：%s，返回值：%s，' % ('pop',stack.pop()), '当前栈：%s，最小值：%s' % (stack, stack.min()))
print('操作：%s，返回值：%s，' % ('pop',stack.pop()), '当前栈：%s，最小值：%s' % (stack, stack.min()))
