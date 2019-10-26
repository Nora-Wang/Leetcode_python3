Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

Example
Example 1:

Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]
Example 2:

Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]
Challenge
O(logn + k) time

Notice
The value k is a non-negative integer and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 10^4
Absolute value of elements in the array will not exceed 10^4


思路：
直接在数组中二分查找 target, 如果不存在则返回大于 target 的最小的或者小于 target 的最大的元素均可.
然后使用两根指针从该位置开始向两端遍历, 每次把差值比较小的元素放入答案中然后将该指针向边界方向移动一下即可.

注意：
while循环中，判断start和end的值是否满足范围要求，若不满足，则直接从尾到头或从头到尾的一次遍历即可；若满足再判断start和end与target的差值



code:
lintcode version
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        #二分法模板，找到start和end的位置
        if len(A) == 0:
            return -1
        
        start = 0
        end = len(A) - 1
        result = []
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        
        #用while循环找k个值
        while len(result) < k:
            #一重判断：start和end是否在取值范围内，若否，则直接顺序取值即可
            if start < 0:
                result.append(A[end])
                end += 1
            elif end > len(A) - 1:
                result.append(A[start])
                start -= 1
            else:
                #二重判断：在A[end]与A[start]中，取与target差值较小的值
                dif_start = target - A[start]
                dif_end = A[end] - target
                if dif_end < dif_start:
                    result.append(A[end])
                    end += 1
                else:
                    result.append(A[start])
                    start -= 1
                
        return result
            
            
            
            
            
leetcode version
insert() 函数用于将指定对象插入列表的指定位置list.insert(index, obj)。当index=0时，可用于从头插入列表。
append是从尾部插入列表
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if len(arr) == 0:
            return []
        
        start = 0
        end = len(arr) - 1
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if arr[mid] <= x:
                start = mid
            else:
                end = mid

        result = []
        while len(result) < k:
            if start < 0:
                result.append(arr[end])
                end += 1
            elif end > len(arr) - 1:
                result.insert(0, arr[start])
                start -= 1
            else:
                dif_start = x - arr[start]
                dif_end = arr[end] - x
                if dif_start <= dif_end:
                    result.insert(0, arr[start])
                    start -= 1
                else:
                    result.append(arr[end])
                    end += 1
        return result
