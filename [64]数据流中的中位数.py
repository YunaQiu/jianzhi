# -*- coding: utf-8 -*-
'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''

import heapq
# 注意：python2没有最大堆，以及python3.7的heapq并没有最大堆对应的push方法
class Solution:
    def __init__(self):
        self.stream = []
        self.small = []
        self.large = []

    def insert(self, num):
        self.stream.append(num)
        if len(self.small) == 0:
            self.small = [num]
        elif num <= self.small[0]:
            self.small.append(num)
            heapq._heapify_max(self.small)
            if len(self.small) > len(self.large) + 1:
                x = heapq._heappop_max(self.small)
                heapq.heappush(self.large, x)
        else:
            heapq.heappush(self.large, num)
            if len(self.large) > len(self.small):
                x = heapq.heappop(self.large)
                self.small.append(x)
                heapq._heapify_max(self.small)

    def median(self):
        if len(self.small) == 0:
            return None
        if len(self.small) == len(self.large):
            return (self.small[0] + self.large[0]) / 2
        return self.small[0]

    def __str__(self):
        return '%s%s' % (self.small[::-1], self.large)

'''
思路：因为不能保证当前输入的数字是否会成为未来的中位数，所以需要将数据流中的数字全部存储下来。为了方便取出中位数，可以将排序后偏小的半边数据用一个容器存储，偏大的半边数据用另一个容器存储。可以选用最大最小堆作为容器。对于新加入的数字，若比中位数大则插入大堆，若插入后大堆的长度超过小堆两个数，则将大堆的最小值插入到小堆中。
边界：数据流为空时，有奇数个数字，偶数个数字，不断插入递增值，不断插入递减值。
'''
# 测试用例
s = Solution()
print('数据流：%s，输出：%s，答案：%s' % (s.stream, s.median(), None))
s.insert(4)
print('数据流：%s，输出：%s，答案：%s' % (s.stream, s.median(), 4))
s.insert(5)
print('数据流：%s，输出：%s，答案：%s' % (s.stream, s.median(), 4.5))
s.insert(6)
print('数据流：%s，输出：%s，答案：%s' % (s.stream, s.median(), 5))
s.insert(7)
print('数据流：%s，输出：%s，答案：%s' % (s.stream, s.median(), 5.5))
s.insert(3)
print('数据流：%s，输出：%s，答案：%s' % (s.stream, s.median(), 5))
s.insert(2)
s.insert(2)
s.insert(1)
s.insert(2)
s.insert(2)
print('数据流：%s，输出：%s，答案：%s' % (s.stream, s.median(), 2.5))
