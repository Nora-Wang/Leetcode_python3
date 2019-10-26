题目：
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).


思路：结合153题，再加一个target。所有情况分析清楚！
                        递增数组：
                                      ↗
                                    ↗
                                  ↗
                                ↗
                              ↗
                            ↗
                          ↗
                        ↗
                        旋转数组，分成两段上升数组：
                                      ↗|
                                    ↗  |
                                  ↗    |
                                ↗      |
                              ↗        |
                        ---------------|------------------
                                       |    ↗
                                       |  ↗
                                       |↗
                              ↑     ↑        ↑
                            start  mid      end
                            第一段           第二段
二分法，mid和end比较：
1. nums[mid] < nums[start]：
	mid在第二段上升区间，跟target比较：
		1. 如果target在start和mid之间，且start>mid时，start= mid
		2. 否则，end = mid
2. nums[start] < nums[mid]：
	mid在第一段上升区间，跟target比较：
		1. 如果target在mid和end之间，且start<mid时，end= mid
		2. 否则，start = mid

                                              s>m                         s<m
                                       t>m         t<m               t>m         t<m
                                   t>s     t<s  t>s    t<s      t>s     t<s  t>s    t<s
                                   e=m     s=m  不存在  e=m      s=m    不存在 e=m    s=m
         

#######第二次做没有考虑清楚如果target在nums[0]的位置时，该怎么处理。

#######有两种方法。个人比较接受的方法是在一开始判断一下nums[0] == target。因为。。。。第二种我是想不到的。。。。。

code：
lintcode version
1.记住先判断mid在哪一侧(A[start] < A[mid],即判断mid是在start那侧还是end那侧)
!!!!!2.A[start] <= target < A[mid]和A[end] >= target > A[mid]的等号
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if len(A) == 0:
            return -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            if A[start] < A[mid]:
		#只用判断target存在于单调性的一侧的情况
	#########等号：因为已不存在A[mid] == target的情况，但当A[start]=target时，若不加=，则执行start = mid，新mid会变到另一侧，
	#########这时target将不在取值范围[start,end]内
                if A[start] <= target < A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[end] >= target > A[mid]:
                    start = mid
                else:
                    end = mid
        print(start,end)
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1





leetcode version
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
   # version 1
        if (len(nums) == 0):
            return -1
        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) / 2
            if (target == nums[mid]):
                return mid
            #第一段
            if (nums[start] > nums[mid]):
                if (target > nums[mid] and target < nums[start]):
                    start = mid
                else:
                    end = mid
            #第二段
            else:
                if (target < nums[mid] and target > nums[start]):
                    end = mid
                else:
                    start = mid
        #若没有rotated
        if (nums[0] == target):
            return 0
        if (nums[start] == target):
            return start
        if (nums[end] == target):
            return end
        return -1


   # version 2简化版 96%
        if (len(nums) == 0):
            return -1
########方法1
	if(nums[0] == target):
            return 0


        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) / 2
            if (target == nums[mid]):
                return mid
	
            if (nums[start] > nums[mid]):
                if (nums[start] > target > nums[mid]):
                    start = mid
                else:
                    end = mid
            else:
#########方法2 加等号
                # 等号原因：若target出现在nums的第一个或最后一个元素，没有等号则直接返回-1；例[1, 3, 5], 1
                if (nums[start] <= target < nums[mid]):
                    end = mid
                else:
                    start = mid

        #例如[1], 1 or [1, 2], 1
        #若无if(start/end)语句，则直接返回-1
        if (nums[start] == target):
            return start
        if (nums[end] == target):
            return end

        return -1
