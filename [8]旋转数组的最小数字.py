# -*- coding: utf-8 -*-

'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray)==0:
            return 0
        if len(rotateArray)==1:
            return rotateArray[0]
        if rotateArray[0] < rotateArray[-1]:
            return rotateArray[0]
        if len(rotateArray)==2:
            return rotateArray[1]
        return self.findMinNum(rotateArray, 0, len(rotateArray)-1)

    def findMinNum(self, rotateArray, headIdx, tailIdx):
        if headIdx == tailIdx-1:
            return rotateArray[tailIdx]
        midIdx = (headIdx + tailIdx) // 2
        if rotateArray[headIdx] == rotateArray[tailIdx] and rotateArray[headIdx] == rotateArray[midIdx]:
            return self.searchMinNum(rotateArray)
        if rotateArray[headIdx] <= rotateArray[midIdx]:
            return self.findMinNum(rotateArray, midIdx, tailIdx)
        else:
            return self.findMinNum(rotateArray, headIdx, midIdx)
    def searchMinNum(self, rotateArray):
        minNum = rotateArray[0]
        for x in rotateArray[1:]:
            if x < minNum:
                minNum = x
        return minNum

'''
思路：采用二分排序，若中间数大于等于第一个数，则说明最小元素在后半部分，反之在前半部分。特殊情况：第一个数、最后一个数、中间数均相等，则无法判断，需直接遍历。若最后一个数比第一个数大，则说明旋转长度为0，第一个数就是最小值。
边界：
长度为0/1/2/3的数组
无旋转的数组
第一个数、中间数、最后数相同的数组：最小值在前半段/后半段/所有值相同
'''
# 测试用例
s = Solution()
print('输入：%s\t输出：%s\t答案：%s' % ([], s.minNumberInRotateArray([]), 0))
print('输入：%s\t输出：%s\t答案：%s' % ([1], s.minNumberInRotateArray([1]), 1))
print('输入：%s\t输出：%s\t答案：%s' % ([2,1], s.minNumberInRotateArray([2,1]), 1))
print('输入：%s\t输出：%s\t答案：%s' % ([2,1,2], s.minNumberInRotateArray([2,1,2]), 1))
print('输入：%s\t输出：%s\t答案：%s' % ([1,2,3,4], s.minNumberInRotateArray([1,2,3,4]), 1))
print('输入：%s\t输出：%s\t答案：%s' % ([2,2,3,4,1,2], s.minNumberInRotateArray([2,2,3,4,1,2]), 1))
print('输入：%s\t输出：%s\t答案：%s' % ([2,2,2,4,1,2], s.minNumberInRotateArray([2,2,2,4,1,2]), 1))
print('输入：%s\t输出：%s\t答案：%s' % ([2,1,1,2,2,2,2], s.minNumberInRotateArray([2,1,1,2,2,2,2]), 1))
print('输入：%s\t输出：%s\t答案：%s' % ([2,2,2,2,2,2,2], s.minNumberInRotateArray([2,2,2,2,2,2,2]), 2))
