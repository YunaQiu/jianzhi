# -*- coding: utf-8 -*-
'''
从一副扑克牌中随机抽取5张牌，其中王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
'''

def isContinue(nums):
    if len(nums) != 5:
        return False
    nums = sorted(nums)
    zero = 0
    for i,x in enumerate(nums):
        if x == 0:
            zero += 1
        elif i>0 and nums[i-1] > 0:
            diff = x - nums[i-1]
            if diff == 0 or diff-1 > zero:
                return False
            else:
                zero -= diff-1
    return True


'''
思路：先对五张牌排序，然后算非0值部分的数字序列的差值，若差值为0，不可能顺子；然后记录差值大于1的部分，再求和。若和大于0的张数，则为false，否则为true
边界：不等于5张，没有王，正好顺子，有王且其余是顺子，缺张数正好为王个数，缺张数大于王的个数，有重复牌
'''
print('输入：%s，输出：%s，答案：%s' % ([4,1,6], isContinue([4,1,6]), False))
print('输入：%s，输出：%s，答案：%s' % ([4,1,2,5,6], isContinue([4,1,2,5,6]), False))
print('输入：%s，输出：%s，答案：%s' % ([4,1,2,5,3], isContinue([4,1,2,5,3]), True))
print('输入：%s，输出：%s，答案：%s' % ([4,0,2,5,3], isContinue([4,0,2,5,3]), True))
print('输入：%s，输出：%s，答案：%s' % ([4,1,0,0,3], isContinue([4,1,0,0,3]), True))
print('输入：%s，输出：%s，答案：%s' % ([4,1,5,0,0], isContinue([4,1,5,0,0]), True))
print('输入：%s，输出：%s，答案：%s' % ([4,1,6,0,0], isContinue([4,1,6,0,0]), False))
print('输入：%s，输出：%s，答案：%s' % ([4,3,6,4,0], isContinue([4,3,6,4,0]), False))
