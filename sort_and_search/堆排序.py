# -*- coding: utf-8 -*-
'''
堆：用列表表示的完全二叉树，其中父节点的值一定大于等于子节点的值
堆插入：将新节点插入到列表的最末端，然后自下而上进行对比调整，直至没有位置交换。
堆删除：即删除堆顶元素。将堆顶与堆末尾元素对调，删除末尾元素，然后再对堆进行自顶向下的对比调整。
堆建立：从列表二分之一处（即最后一个中间节点）开始从后往前遍历，每次都进行一次以该节点为父节点的自顶向下调整。
堆排序：将数组构造成最大堆，然后递归进行堆删除操作
时间复杂度：
堆插入、堆删除、堆调整：O(logN)
堆建立：O(N)
堆排序：O(NlogN)    //构建堆O(N)+递归删除堆O(N*logN)=O(NlogN)
最优复杂度：O(NlogN)
最差复杂度：O(NlogN)
空间复杂度：O(1)
稳定性：不稳定
'''
def siftdown(heap, root, endIdx=None, type='min'):
    endIdx = len(heap)-1 if endIdx is None else endIdx
    if root > (endIdx-1) // 2 or root < 0:
        return
    if type == 'min':
        idx = 2*root+1 if 2*root+2 > endIdx or heap[2*root+1] < heap[2*root+2] else 2*root+2
        if heap[idx] < heap[root]:
            heap[root], heap[idx] = heap[idx], heap[root]
            siftdown(heap, idx, endIdx=endIdx, type='min')
    elif type == 'max':
        idx = 2*root+1 if 2*root+2 > endIdx or heap[2*root+1] > heap[2*root+2] else 2*root+2
        if heap[idx] > heap[root]:
            heap[root], heap[idx] = heap[idx], heap[root]
            siftdown(heap, idx, endIdx=endIdx, type='max')

def siftup(heap, pos, type='min'):
    if pos < 1 or pos >= len(heap):
        return
    root = (pos - 1) // 2
    sibl = pos-1 if pos % 2 == 0 else pos+1
    if type == 'min':
        idx = pos if sibl >= len(heap) or heap[pos] < heap[sibl] else sibl
        if heap[idx] < heap[root]:
            heap[root], heap[idx] = heap[idx], heap[root]
            siftup(heap, root, type='min')
    elif type == 'max':
        idx = pos if sibl >= len(heap) or heap[pos] > heap[sibl] else sibl
        if heap[idx] > heap[root]:
            heap[root], heap[idx] = heap[idx], heap[root]
            siftup(heap, root, type='max')

def heapBuild(arr, type='min'):
    if len(arr) < 2:
        return
    for i in range(len(arr)//2 - 1, -1, -1):
        siftdown(arr, i, type=type)

def heapPush(heap, item, type='min'):
    heap.append(item)
    siftup(heap, len(heap)-1, type=type)

def heapPop(heap, type='min'):
    if len(heap) == 0:
        return None
    heap[0], heap[-1] = heap[-1], heap[0]
    item = heap.pop()
    siftdown(heap, 0, type=type)
    return item

def heapSort(arr):
    if len(arr) < 2:
        return arr
    heapBuild(arr, type='max')
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        siftdown(arr, 0, type='max', endIdx=i-1)
    return arr

# 测试用例
print('输入：%s，输出：%s，答案：%s' % ([], heapSort([]), []))
print('输入：%s，输出：%s，答案：%s' % ([2], heapSort([2]), [2]))
print('输入：%s，输出：%s，答案：%s' % ([2,1], heapSort([2,1]), [1,2]))
print('输入：%s，输出：%s，答案：%s' % ([0,1], heapSort([0,1]), [0,1]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1], heapSort([0,3,1]), [0,1,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3], heapSort([0,3,1,3]), [0,1,3,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3,3], heapSort([0,3,1,3,3]), [0,1,3,3,3]))
print('输入：%s，输出：%s，答案：%s' % ([0,3,1,3,0,3], heapSort([0,3,1,3,0,3]), [0,0,1,3,3,3]))

# 堆的测试用例
heap = []
print('操作：%s，输出：%s，堆：%s' % ('建空堆', heapBuild(heap), heap))
heap = [2]
print('操作：%s，输出：%s，堆：%s' % ('建长度为1的堆', heapBuild(heap), heap))
heap = [1,3,1,5,6,2,0,7,4]
print('操作：%s，输出：%s，堆：%s' % ('建最小堆', heapBuild(heap), heap))
print('操作：%s，输出：%s，堆：%s' % ('插入3', heapPush(heap, 3), heap))
print('操作：%s，输出：%s，堆：%s' % ('删除值', heapPop(heap), heap))
print('操作：%s，输出：%s，堆：%s' % ('插入-2', heapPush(heap,-2), heap))
print('操作：%s，输出：%s，堆：%s' % ('插入10', heapPush(heap,10), heap))
heap = [1,3,1,5,6,2,0,7,4]
print('操作：%s，输出：%s，堆：%s' % ('建最大堆', heapBuild(heap, type='max'), heap))
print('操作：%s，输出：%s，堆：%s' % ('插入3', heapPush(heap, 3, type='max'), heap))
print('操作：%s，输出：%s，堆：%s' % ('删除值', heapPop(heap, type='max'), heap))
print('操作：%s，输出：%s，堆：%s' % ('插入-2', heapPush(heap,-2, type='max'), heap))
print('操作：%s，输出：%s，堆：%s' % ('插入10', heapPush(heap,10, type='max'), heap))
