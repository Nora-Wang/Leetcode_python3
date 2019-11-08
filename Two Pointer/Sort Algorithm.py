1. Quick Sort
不稳定Unstable
时间复杂度：O(nlogn) ~ O(n^2)
空间复杂度：O(logn)~O(n)
O(nlogn) 空间复杂度O（logn） 不稳定

主体思路：
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
