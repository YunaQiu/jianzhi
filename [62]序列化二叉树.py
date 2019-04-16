# -*- coding: utf-8 -*-
'''
请实现两个函数，分别用来序列化和反序列化二叉树
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        result = "" if self.left is None else "(%s)<=" % self.left
        result += str(self.val)
        result += "" if self.right is None else "=>(%s)" % self.right
        return result

def serialize(tree, strList=None):
    # 注意：默认参数只能是不可变对象，因此不能直接默认为空列表
    strList = [] if strList is None else strList
    if tree is None:
        strList.append('N')
    else:
        strList.append(str(tree.val))
        serialize(tree.left, strList)
        serialize(tree.right, strList)
    return ','.join(strList)

def deserialize(s):
    if isinstance(s, str):
        s = s.split(',')
    x = s.pop(0)
    if x == 'N':
        return None
    x = int(x)
    tree = TreeNode(x)
    tree.left = deserialize(s)
    tree.right = deserialize(s)
    return tree

'''
思路：序列化指的是将树的结构用字符串记录下来。反序列化则是根据该字符串还原为树。可以采用前序遍历方式记录树节点，但是需将空的子节点也记录下来才能保证唯一还原。
如：
   1
  / \
 4   2
 \  / \
  6 3  5
序列化为：1,4,N,6,N,N,2,3,N,N,5,N,N
边界：空树，只有左子树，只有右子树，满树，不平衡树
'''
# 测试用例
print('输入：%s，序列化：%s，反序列化：%s' % (None, serialize(None), deserialize(serialize(None))))
node1 = TreeNode(1)
print('输入：%s，序列化：%s，反序列化：%s' % (node1, serialize(node1), deserialize(serialize(node1))))
node2 = node1.left = TreeNode(2)
print('输入：%s，序列化：%s，反序列化：%s' % (node1, serialize(node1), deserialize(serialize(node1))))
node3 = node2.left = TreeNode(3)
print('输入：%s，序列化：%s，反序列化：%s' % (node1, serialize(node1), deserialize(serialize(node1))))
node1.left = None
node1.right = node2
print('输入：%s，序列化：%s，反序列化：%s' % (node1, serialize(node1), deserialize(serialize(node1))))
node4 = node1.left = TreeNode(4)
print('输入：%s，序列化：%s，反序列化：%s' % (node1, serialize(node1), deserialize(serialize(node1))))
node5 = node2.right = TreeNode(5)
print('输入：%s，序列化：%s，反序列化：%s' % (node1, serialize(node1), deserialize(serialize(node1))))
node6 = node4.right = TreeNode(6)
print('输入：%s，序列化：%s，反序列化：%s' % (node1, serialize(node1), deserialize(serialize(node1))))
node7 = node4.left = TreeNode(7)
print('输入：%s，序列化：%s，反序列化：%s' % (node1, serialize(node1), deserialize(serialize(node1))))
