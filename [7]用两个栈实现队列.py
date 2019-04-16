# -*- coding:utf-8 -*-
'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型
'''

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def __str__(self):
        return '%s' % (self.stack2[::-1] + self.stack1)
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if len(self.stack2)>0:
            return self.stack2.pop()
        else:
            self.transform()
            return self.stack2.pop() if len(self.stack2)>0 else None
    def transform(self):
        if len(self.stack1)>0 and len(self.stack2)==0:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop())

'''
思路：第一个栈负责添加元素。若要取出元素，则将栈1的元素依次pop到栈2中，此时栈2中的出栈顺序即为队列的pop顺序。之后就是栈1负责入队，栈2负责出队，栈2若空，就将栈1pop到栈2。若栈1也空，则pop函数返回None
边界：
空队列时添加元素/弹出元素
栈1空，栈2有值时添加元素
栈1有值，栈2空时弹出元素
'''
# 测试用例
que = Queue()
print('初始队列：%s' % que)
print('操作：%s\t返回值：%s\t操作后队列：%s' % ("pop", que.pop(), que))
print('操作：%s\t返回值：%s\t操作后队列：%s' % ("push(1)", que.push(1), que))
print('操作：%s\t返回值：%s\t操作后队列：%s' % ("push(2)", que.push(2), que))
print('操作：%s\t返回值：%s\t操作后队列：%s' % ("pop", que.pop(), que))
print('操作：%s\t返回值：%s\t操作后队列：%s' % ("push(3)", que.push(3), que))
print('操作：%s\t返回值：%s\t操作后队列：%s' % ("pop", que.pop(), que))
