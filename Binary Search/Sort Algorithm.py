Quick Select参考215(Two Pointer)

Quick Sort与Merge Sort比较：

1.Quick Sort
从上往下
不稳定Unstable（同样的value时，value1和value2不会按照原数组的顺序被排序，可能排完序的结果为value2，value1）

时间复杂度：O(n) ~ O(n^2) （每次划分都选的头或尾时，为O(n^2)；每次都是中间时，为O(n)）
平均时间复杂度：O(nlogn)
空间复杂度：O(1) (原地排序)
先整体有序，再局部有序：T(n) = 2T(n/2) + O(n)先做O(n),即先partition

2.Merge Sort
从上往下，再从下往上
稳定Stable（同样的value时，value1和value2会按照原数组的顺序被排序）

时间复杂度：O(nlogn) = O(n) + O(nlogn) -> 
O(n)是从上往下在每一层进行partition二分。
第二层为O(1)切一刀，第三层为O(2)切2刀，第四层为O(4)切4刀...最后一层为O(n)切n刀，因此为O(n/2 + n/4 + n/8 +… 1) = O(n)
O(nlogn)是从下往上进行merge。
每一层都会将所有的值遍历一遍O(n) * 因为二分一共会有O(logn)层（类似balanced binary tree）

空间复杂度：O(n)
先局部有序，再整体有序：T(n) = 2T(n/2) + O(n)先做2T(n/2)，即先partition，再做O(n),即后merge




1. Quick Sort

follow up:Quick Select 215. Kth Largest Element in an Array

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
#注意点1:一定要写停止条件
        if start >= end:
            return
        
#注意点2:pivot不能为首尾,不然quick sort的时间复杂度则为最差情况O(n^2)
#注意点3:pivot是value而不是index，因为后面的比较是用的值比较的
        left, right = start, end
        pivot = A[start + (end - start) / 2]
        
        #partition
#注意点4:这里是<=,用<会出现stack overflow，因为后续recursion时可能会出现交集
        while left <= right:
#注意点5:若A[left] <= pivot会出现不均匀的情况stack overflow，当全部都等于pivot时，会直接循环到end
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[end] > pivot:
                right -= 1
                
#注意点6:需要判断一下此时是否满足left <= right，因为可能存在left > right而跳出前面两个while循环的情况
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
                
#注意点7:这里是start与right，left与end配对，因为前面while循环结束时的情况为left>right
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
        
  #注意点1:temp在初始化的时候不能写成temp = [] * len(A)，会出bug:list assignment index out of range
        #用temp来记录每次的排序，最后再将temp赋值给A，因此merge sort会比quick sort多耗费O(n)的extra space
        temp = [0] * len(A)
        self.mergeSort(A, 0, len(A) - 1, temp)
        
    def mergeSort(self, A, start, end, temp):
        
  #注意点2:记得一定要加上这部分，不然会maximum recursion depth exceeded
        #这里的原因是在divide二分时，当只有一个元素时就不用分了
        if start == end:
            return
        
  #注意点3:middle要去整，因为后续会当作index用
        #这样写是为了避免溢出（虽然python并不存在这种问题，因为python在可能出现溢出时，系统会自动增大存储空间，以避免溢出的出现）
        #溢出是因为当start和end都很大时,(start + end)的值可能会很大，因此造成溢出
        #而这样写，end和start首先是保证不会溢出的，而end - start也肯定不会溢出，这样就保证整个等式不会造成溢出的情况
        middle = start + (end - start) // 2
        
        self.mergeSort(A, start, middle, temp)
        self.mergeSort(A, middle + 1, end, temp)
        
        self.merge(A, start, end, temp)
        
    def merge(self, A, start, end, temp):
  #同注意点3
        middle = start + (end - start) // 2
        leftIndex = start
        rightIndex = middle + 1
        
  #注意点4:index要赋值为start或者leftIndex，因为temp要从头开始赋值
        index = start
        
        #两边比较后将小一点的值放入temp
  #注意点5:注意<=,每个值都需要被遍历到
        while leftIndex <= middle and rightIndex <= end:
            if A[leftIndex] < A[rightIndex]:
                temp[index] = A[leftIndex]
                leftIndex += 1
            else:
                temp[index] = A[rightIndex]
                rightIndex += 1
            index += 1
            
        #当一边已经遍历完，而另一边还有余时，将其剩余部分全部添加进temp
        while leftIndex <= middle:
            temp[index] = A[leftIndex]
            index += 1
            leftIndex += 1
        while rightIndex <= end:
            temp[index] = A[rightIndex]
            index += 1
            rightIndex += 1
        
        #将temp再赋值给A
  #注意点6:range一定要是[start, end + 1],python左闭右开原则；另外不能用len(temp)或者len(A),取值不对
        for index in range(start, end + 1):
            A[index] = temp[index]
 
