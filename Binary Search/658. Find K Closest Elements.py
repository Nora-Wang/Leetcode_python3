Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:

Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:

Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:

The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 10^4
Absolute value of elements in the array and x will not exceed 10^4
UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.


思路：
直接在数组中二分查找 target, 如果不存在则返回大于 target 的最小的或者小于 target 的最大的元素均可.

然后使用两根指针从该位置开始向两端遍历, 每次把差值比较小的元素放入答案中然后将该指针向边界方向移动一下即可.


# 23/09/2024
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = self.binary_search(arr, x)
        
        left, right = index - 1, index + 1
        for _ in range(k - 1):
            if left < 0:
                right += 1
                continue
                
            if right >= len(arr):
                left -= 1
                continue
            
            if abs(arr[left] - x) > abs(arr[right] - x):
                right += 1
            else:
                left -= 1
        
        return arr[left + 1:right]
    
    def binary_search(self, arr, target):
        start, end = 0, len(arr) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if arr[mid] == target:
                return mid
            
            if arr[mid] < target:
                start = mid
            else:
                end = mid
                
        if arr[start] == target:
            return start
        if arr[end] == target:
            return end
        
        return end if abs(arr[start] - target) > abs(arr[end] - target) else start
                


#06/15/2020
#time: O(logn + k), space: O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        
        #找到最接近target的index
        x_index = self.find_target(arr, x)
        
        #背向双指针
        left, right = x_index - 1, x_index + 1
        k -= 1
        
        while k > 0 and left >= 0 and right < len(arr):
            if x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
            
            k -= 1
            
        while k > 0 and left >= 0:
            left -= 1
            k -= 1
        while k > 0 and right < len(arr):
            right += 1
            k -= 1
        
        #注意这里left和right代表下一个用于判断的值,因此真正valid的数应该在left + 1 ~ right - 1之间
        return arr[left + 1:right]
        
        
    
    def find_target(self, arr, target):
        start, end = 0, len(arr) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if arr[mid] == target:
                return mid
            
            if arr[mid] > target:
                end = mid
            else:
                start = mid
        
        return start if abs(arr[start] - target) <= abs(arr[end] - target) else end
        
        

#3.13 Version
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = self.find_index(arr, x)
        
        res = [arr[index]]
        left, right = index - 1, index + 1
        
        while left >= 0 and right < len(arr) and len(res) < k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
                
        while left >= 0 and len(res) < k:
            res.append(arr[left])
            left -= 1
        
        while right < len(arr) and len(res) < k:
            res.append(arr[right])
            right += 1
        
        return sorted(res)

    def find_index(self, arr, x):
        start, end = 0, len(arr) - 1
        index = sys.maxsize
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if arr[mid] == x:
                index = mid
                break
            
            if arr[mid] < x:
                start = mid
            else:
                end = mid
        
        if index == sys.maxsize:
            return start if abs(arr[start] - x) <= abs(arr[end] - x) else end
        
        return index






code:
leetcode version
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        #利用二分法模板找start和end的位置
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
            #当start和end不在取值范围内时，则相当于单调递增or单调递减，这时直接按顺序取值即可
            if start < 0:
                result.append(arr[end])
                end += 1
            elif end > len(arr) - 1:
                result.insert(0, arr[start])
                start -= 1
                
            #当start和end在取值范围内时，则比较start和end与target的差值，差值较小者被append进result
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
        
        
        
lintcode version
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
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
        
        while len(result) < k:
            if start < 0:
                result.append(A[end])
                end += 1
            elif end > len(A) - 1:
                result.append(A[start])
                start -= 1
            else:
                dif_start = target - A[start]
                dif_end = A[end] - target
                if dif_end < dif_start:
                    result.append(A[end])
                    end += 1
                else:
                    result.append(A[start])
                    start -= 1
                
        return result
            
            
            
