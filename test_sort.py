#-------------------------------------------------------------------------------
##notes: 据书上的测试图来看，在数据量小于20的时候，插入排序具有最好的性能。当大于20时，快速排序具有最好的性能，归并(merge sort)和堆排序(heap sort)也望尘莫及，尽管复杂度都为nlog2(n)。
################################################
###insertion sort alg
###complexity:  Ɵ(n2)
###Summay: there is a key in i pos, numbers in pre i is sorted.
###        from i -1 to 0, insert the key to the right pos, all the post insert pos
###        move to next pos
##有序区因为插入元素不断后移，类似抓扑克牌排序
################################################
def insertionsort(sortlist):
    n = len(sortlist)
    #print n
    for i in range(1,n):   # range means  1<=i<n
        j= i -1
        key = sortlist[i]
        while( key < sortlist[j] and j>=0):
            sortlist[j+1] = sortlist[j]
            j=j-1

        sortlist[j+1]=key
        #print sortlist

################################################
## Recursively Merge sort A[1....n]
## 1.if n= 1 done      Ɵ(1)
## 2.Recursively sort
## A[1...[n/2]]] and A[[n/2]+1....n]   2T(n/2)
## Merge 2 sorted list            Ɵ(n)
##  Recursivon tree T(n) = 2T(n/2)+constant
##  Ɵ(nlogn)
## 归并排序是O(nlgn）时间，需要O(n)的空间
################################################
def mergesort(rlist):  # Iteration
    length = len(rlist)

    for i in xrange(1,length,2*i): # // 子数组的大小i初始为1，每轮翻倍
        left = 0
        while(left + i < length): # 后一个子数组存在(需要归并)
            mid = left+i -1
            if i+mid < length:
                right = mid+i
            else:
                right = length-1

            _merge2(srclist, left, mid, right)

            left=right+1



def merge_sort2(sortlist,start,end):   #Recursion

    if start<end:
        middle = (start+end)/2

        merge_sort2(sortlist,start,middle)
        merge_sort2(sortlist,middle+1,end)
        _merge2(sortlist, start, middle, end)


def _merge2(srclist, start, middle, end):
## need size space to implement merge
    size = end -start+1
    dstlist = [0]*size
    left = start
    right = middle+1
    i = 0

    while (left <= middle and right <= end): #依次拷贝到dst
        if srclist[left] < srclist[right]:
            dstlist[i]=srclist[left]
            left=left +1
        else:
            dstlist[i]=srclist[right]
            right = right +1

        i = i+1


    while (left <= middle): #如果有剩下的左表拷贝到dst
        dstlist[i]=srclist[left]
        left=left +1
        i = i+1

    while (right <= end): #或者有剩下右表依次拷贝到dst
        dstlist[i]=srclist[right]
        right = right +1
        i = i+1

    #把排续好的dst拷贝到srclist
    j=start
    k=0
    while(j<=end and k<=size):
        srclist[j]=dstlist[k]
        j=j+1
        k=k+1
    del dstlist

################################################
### Quicksort: dvide and conquer
### _partion():Ɵ(n)
### O(nlgn）
##把所有比基准值小的元素放在基准前面，所有比基准值大的元素放在基准的后面（相同的数可以到任一边），这个称为分区(partition)操作。
################################################

def quicksort(sortlist,low,high):
    if low < high:
        key_index = _partion(sortlist,low,high)
        quicksort(sortlist,low,key_index-1)
        quicksort(sortlist,key_index +1,high)

def _partion(sortlist,low,high):# 划分函数
    key = sortlist[low]

    while low < high:
        while low < high and sortlist[high] >= key:
            high = high -1
        if low < high:
            sortlist[low] = sortlist[high]

        while low < high and sortlist[low] <= key:
            low = low +1
        if low < high:
            sortlist[high] = sortlist[low]

    sortlist[low] = key
    return low


################################################
## heap sort
## complexity:  Ɵ(nlogn)
## 大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]
## 小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]
## 步骤1、建堆（升序建大堆，降序建小堆）；
##     2、交换数据，堆顶和堆尾交换，无序区减1；3、向下调整。
## 最后一个非终端元素的下标是[n/2]向下取整，所以筛选只需要从第[n/2]向下取整个元素开始，从后往前进行调整。
##// 分类 -------------- 内部比较排序
##// 数据结构 ---------- 数组
##// 最差时间复杂度 ---- O(nlogn)
##// 最优时间复杂度 ---- O(nlogn)
##// 平均时间复杂度 ---- O(nlogn)
##// 所需辅助空间 ------ O(1)
##// 稳定性 ------------ 不稳定
################################################
def _make_max_heap(heap):
    heapsize = len(heap)
    non_leavenode_start = heapsize/2 -1
    #print non_leavenode_start
    for i in xrange(non_leavenode_start,-1,-1):  #从第[n/2]向下取整个元素开始，从后往前进行调整到堆顶
        _adjust_max_heap(heap,i,heapsize)


def _adjust_max_heap(heap,i,n):  # n is length of heap
    left_child = 2*i + 1
    right_child = left_child + 1
    max = i

    if left_child < n and heap[max] < heap[left_child]:
        max = left_child
    if right_child < n and heap[max] < heap[right_child]:
        max = right_child

    if max != i: #adjust in previous compare,max is left or right child
        heap[max],heap[i] = heap[i],heap[max]
        _adjust_max_heap(heap,max,n)  #往下调整到叶子



def heapsort(heap):
    _make_max_heap(heap)
    print "make a max heap "
    print heap
    print "heap sort"
    for i in range(len(heap) -1,-1,-1):
        heap[0],heap[i]= heap[i],heap[0]
        _adjust_max_heap(heap,0,i)



################################################
## buble sort
## complexity:  Ɵ(n2)
################################################
def bubblesort(sortlist):
    n = len(sortlist)
    for i in range(0,n):
        #print i
        for j in range(0, (n-1-i)):#// 依次比较相邻的两个元素,使较大的那个向后移
            if sortlist[j] > sortlist[j+1]: #// 依次比较相邻的两个元素,使较大的那个向后移
                sortlist[j],sortlist[j+1]=sortlist[j+1],sortlist[j]



################################################
##
## select sort
## O（n2）
## 每一趟在n-i+1（i=1，2，…n-1）个记录中选取关键字最小的记录作为有序序列中第i个记录
################################################
def selectsort2(sortlist):
    n = len(sortlist)
    i = 0
    for i in range(n/2):

        min = i
        max = n- i -1

        #if max < min, swap them firstly
        if sortlist[min]>sortlist[max]:
            sortlist[min],sortlist[max]=sortlist[max],sortlist[min]


        j = min+1
        while (j<n-i-1):
            if sortlist[j]<sortlist[min]:
                min = j

            if sortlist[j] > sortlist[max]:
                max = j
            j = j+1

        #set min data
        if min!= i:
            sortlist[min],sortlist[i]=sortlist[i],sortlist[min]

        #set max data
        if max!=n-i-1:
            sortlist[max],sortlist[n-i-1]=sortlist[n-i-1],sortlist[max]







if __name__ == '__main__':
    testlist= [49,38,65,97,76,13,27,49,0,3,8,2]
##    testlist = [6,2,7,3,8,9]
##    testlist = [5,9 ,3, 2, 1, 3, 3,2]
    print testlist
##    insertionsort(testlist)
##    merge_sort2(testlist,0,len(testlist)-1)
##    quicksort(testlist,0,len(testlist)-1)
 ##   bubblesort(testlist)
    heapsort(testlist)
    print testlist




