Quick Sort与Merge Sort比较：

1.Quick Sort
不稳定Unstable（同样的value时，value1和value2不会按照原数组的顺序被排序，可能排完序的结果为value2，value1）
时间复杂度：O(n) ~ O(n^2) （每次划分都选的头或尾时，为O(n^2)；每次都是中间时，为O(n)）
平均时间复杂度：O(nlogn)
空间复杂度：O(1) (原地排序)
先整体有序，再局部有序：T(n) = 2T(n/2) + O(n)先做O(n),即先partition

2.Merge Sort
稳定Stable（同样的value时，value1和value2会按照原数组的顺序被排序）
时间复杂度：O(nlogn)
空间复杂度：O(n)
先局部有序，再整体有序：T(n) = 2T(n/2) + O(n)先做2T(n/2)，再做O(n),即后merge




1. Quick Sort

参考链接：https://www.jianshu.com/p/655db46e161d
1.首先选择一个中间元素pivot = A[start + (right - left) / 2]
2.分别获取除中间元素外的左右两端的索引
3.由左右两端逐渐向中间迭代，每迭代一步比较一下索引中的元素和中间元素，当左边出现比中间元素大的元素的时候，
暂停左边的迭代，当右边迭代出比中间元素小的元素的时候，右边迭代也暂停，交换左右两边的元素
4.重复步骤3，直到左右两边的索引相遇，然后将中间元素移动到中间，这时中间元素左边的元素都比它小，右边的元素都比它大
5.将上面的中间元素左右两边当成两个数组，分别进行上述过程
6.重复以上步骤直到数组不可再分


class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        if not A:
            return None
            
        self.quicksort(A, 0, len(A) - 1)
    
    #left和right比较时，用<=
    #与pivot比较时，不要=
    def quicksort(self, A, start, end):
        if start >= end:
            return
        
        #pivot不能为收尾
        #pivot是value而不是index
        left, right = start, end
        pivot = A[start + (right - left) / 2]
        
        #partition
        #注意这里是<=
        #用<会stack overflow，因为后续recursion时可能会出现交集
        while left <= right:
            #A[left] <= pivot会出现不均匀的情况stack overflow，当全部都等于pivot时，会直接循环到end
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[end] > pivot:
                right -= 1
                
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
                
        #注意这里是start与right，left与end配对，因为前面while循环结束时的情况为left>right
        #此时的A被分为3个部分[start, right],pivot,[left,end]
        self.quicksort(A, start, right)
        self.quicksort(A, left, end)
           


2.Merge Sort

参考链接：https://www.jianshu.com/p/655db46e161d
实现归并排序的另一种方式是从小数组开始归并：
首先我们将数组的每一个元素都当做一个只有一个元素的数组，然后将其两两归并。
然后我们将整个数组的每两个元素都当做一个小数组，然后将其两两归并，然后四个四个归并，依次类推，直到最后归并成一个大数组，排序就完成了。


class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        if not A:
            return None
        
        #用temp来记录每次的排序，最后再将temp赋值给A，因此merge sort会比quick sort多耗费O(n)的extra space
        temp = [0] * len(A)
        self.mergeSort(A, 0, len(A) - 1, temp)
        
    def mergeSort(self, A, start, end, temp):
        if start >= end:
            return
        
        middle = start + (end - start) // 2
        
        self.mergeSort(A, start, middle, temp)
        self.mergeSort(A, middle + 1, end, temp)
        
        self.merge(A, start, end, temp)
        
    def merge(self, A, start, end, temp):
        middle = start + (end - start) // 2
        leftIndex = start
        rightIndex = middle + 1
        index = start
        
        while leftIndex <= middle and rightIndex <= end:
            if A[leftIndex] < A[rightIndex]:
                temp[index] = A[leftIndex]
                leftIndex += 1
            else:
                temp[index] = A[rightIndex]
                rightIndex += 1
            index += 1
            
        #当还有余时，将剩余部分添加进temp
        while leftIndex <= middle:
            temp[index] = A[leftIndex]
            index += 1
            leftIndex += 1
            
        while rightIndex <= end:
            temp[index] = A[rightIndex]
            index += 1
            rightIndex += 1
        
        #将temp再赋值给A
        for index in range(start, end + 1):
            A[index] = temp[index]
 
