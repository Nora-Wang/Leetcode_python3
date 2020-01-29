Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?


用heap做,将中位数以及中位数之前的数存入max_heap,将中位数之后的数存入min_heap
这样求中位数时,要不就是max_heap中的最大值,要不就是（max_heap的最大值 + min_heap的最小值）/ 2


code:
import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        #最大堆放从大到小（中间到最小），最小堆放从小到大（中间到最大） 
        #注意最大堆里的数都是相反数（负数）
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """ 
        #先放到最大堆里，再放最小堆，保持两个堆平衡
        #这样的结果为中位数以及中位数之前的数被存入max_heap,而中位数之后的数被存入min_heap
        if len(self.max_heap) <= len(self.min_heap):
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        #每次放完以后要判断，最大堆的第一个（堆中最大值）是不是大于最小堆的第一个（堆中最小值） 
        #如果大，则需将两个数交换位置，保持最大堆和最小堆都是从中位数分开的 
        if self.min_heap and self.min_heap[0] < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            
        

    def findMedian(self):
        """
        :rtype: float
        """
        #第一轮最小堆里没东西时，返回最大堆第一个数
        if not self.min_heap:
            return -self.max_heap[0]
        
        #如果两堆一样长证明需要计算中位数，中间的数分别都是最大最小堆的第一个数 
        if len(self.min_heap) == len(self.max_heap):
            return (float(self.min_heap[0]) - self.max_heap[0]) / 2
        
        #否则直接返回最大堆的第一个
        return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
