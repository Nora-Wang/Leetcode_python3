Quick Select参考215(Two Pointer)

Quick Sort与Merge Sort比较：

1. Quick Sort
从上往下
不稳定Unstable（同样的value时，value1和value2不会按照原数组的顺序被排序，可能排完序的结果为value2，value1）
pivot的值可以任意取，只要最后满足整个区间的左边都小于等于pivot，右边都大于等于pivot即可。
实际上快排的pivot值本就是随机选择一个存在的元素，只有在随机取的情况下才不容易达到O(n^2)的最坏复杂度。但通常可以取左边界，右边界或者中间的值。

时间复杂度：O(n) ~ O(n^2) （每次划分都选的头或尾时，为O(n^2)；每次都是中间时，为O(n)）
平均时间复杂度：O(nlogn)

空间复杂度：O(1) (原地排序)
先整体有序，再局部有序：T(n) = 2T(n/2) + O(n)先做O(n),即先partition

2. Merge Sort
从上往下，再从下往上
稳定Stable（同样的value时，value1和value2会按照原数组的顺序被排序）

时间复杂度：O(nlogn) = O(n) + O(nlogn) -> 
O(n)是从上往下在每一层进行partition二分。
第二层为O(1)切一刀，第三层为O(2)切2刀，第四层为O(4)切4刀...最后一层为O(n)切n刀，因此为O(n/2 + n/4 + n/8 +… 1) = O(n)
O(nlogn)是从下往上进行merge。
每一层都会将所有的值遍历一遍O(n) * 因为二分一共会有O(logn)层（类似balanced binary tree）

空间复杂度：O(n)
先局部有序，再整体有序：T(n) = 2T(n/2) + O(n)先做2T(n/2)，即先partition，再做O(n),即后merge

3. Selection Sort
每次都选择当前rest array中的最小值，swap到rest array的头
Given an array of integers, sort the elements in the array in ascending order. 
The selection sort algorithm should be used to solve this problem.

time: O(n^2), space: O(1)
        
        
4. Insert Sort
将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
参考链接：https://www.runoob.com/w3cnote/insertion-sort.html
    
time: O(n^2), space: O(1)
        

        
        
        
        

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
        #问题1：这里的end case为什么不能是start== end ？
        #写法差异，考虑到下面问题2的地方，会存在最后一次判断left==right，接着left+=1,right-=1，于是start==end这种情况将不会出现.
        if start > end:
            return
        
#注意点1:pivot不能为首尾,不然quick sort的时间复杂度则为最差情况O(n^2)
#注意点2:pivot是value而不是index，因为后面的比较是用的值比较的
        left, right = start, end
        pivot = A[start + (end - start) / 2]
        
        #partition
        
        #问题2：这里的while条件为什么是left <= right？为什么要加等号？
        #同样是写法差异。因为问题1处没有考虑等于。这里将left=right的情况考虑在一起。
        #left==right意味着当前区间中只有一个element，其实是整个区间已经有序了，不需要再分治了，若再继续进行分治则会出现死循环或数组越界的问题。
        while left <= right:
        #问题3 : 这里为什么不能是nums[left] <= pivot？
        #边界问题。如果取等号，会发生数组越界。 
        #考虑一组[3,1, 3,2,5]，一开始l=0，r=4，pivot=3若条件为nums[left] <= pivot和nums[right] >= pivot，则最后停下来时l=4, r=3。
        #数组没有任何交换，接着会进入区间[start=0, right=3]，也就是[3, 1, 3, 2]。pivot=1。重复上面步骤，会发现最后l=0, r=-1。
        #继续递归会发生数组越界错误。
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
        #问题4 : 这里结束后，整个nums被分成什么什么样了？是start ~ right, pivot, left ~ end? Why?
        #快排满足“在任意时刻，left左边都小于等于pivot，right右边都大于等于pivot”。
        #所以此时区间被分为[start,right]<=pivot，[left,end]>=pivot
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
        #这里设置一个temp是为了在后续从下往上merge的时候用
        #后续merge是两个有序数组要合并成一个，而这两个sorted array相当于是nums[start, mid]和nums[mid, end].
        #因为当初divide的时候就是利用二分，因此在conquer的时候也是如此merge即可。
        #在nums上没有方便的原地算法（不额外使用空间的算法），因此利用一个temp来暂时存储sort后的结果，在最后再将sort好的结果重新赋给nums
	#这也是归并排序空间复杂度为O(n)的原因。
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
 

3. Selection Sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        for i in range(len(nums)):
            min_index = i
            
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
                    
            nums[i], nums[min_index] = nums[min_index], nums[i]
        
        return nums

    
    
4. Insert Sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        for i in range(1, len(nums)):
            index = i
            
            while index > 0 and nums[index] < nums[index - 1]:
                nums[index], nums[index - 1] = nums[index - 1], nums[index]
                index -= 1
            
        return nums
