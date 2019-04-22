# -*- coding:utf-8 -*-
'''
桶排序：建立K个桶，每个桶存放一定范围内的数据，且桶之间有顺序关系。遍历原数组将元素追加到对应的桶中，再分别对k个桶内的数据进行排序，最后再依次取出各个桶的数据。
时间复杂度：O(N+C)    // C与桶内排序的算法有关，若为比较型排序算法，则下限是O(Nlog(N/K))，若继续叠加桶排序，则是线性复杂度
空间复杂度：O(N+K)
稳定性：稳定
'''

def bucketSort(arr):
    # 假如数字范围为0~99，可按十位数字划分10个桶
    bucket = [[] for i in range(10)]
    for x in arr:
        bucket[toBucketIdx(x)].append(x)
    for i in range(len(bucket)):
        # 看情况选择桶内排序算法
        bucket[i] = sorted(bucket[i])
    resArr = []
    for b in bucket:
        resArr.extend(b)
    return resArr

def toBucketIdx(x):
    return x // 10


# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([], bucketSort([]), []))
print('输入：%s，输出：%s，答案：%s' % ([2], bucketSort([2]), [2]))
print('输入：%s，输出：%s，答案：%s' % ([2,1], bucketSort([2,1]), [1,2]))
print('输入：%s，输出：%s，答案：%s' % ([0,10], bucketSort([0,10]), [0,10]))
print('输入：%s，输出：%s，答案：%s' % ([0,30,1], bucketSort([0,30,1]), [0,1,30]))
print('输入：%s，输出：%s，答案：%s' % ([0,30,10,30], bucketSort([0,30,10,30]), [0,10,30,30]))
print('输入：%s，输出：%s，答案：%s' % ([0,30,10,30,3], bucketSort([0,30,10,30,3]), [0,3,10,30,30]))
print('输入：%s，输出：%s，答案：%s' % ([0,30,10,3,0,30], bucketSort([0,30,10,3,0,30]), [0,0,3,10,30,30]))
