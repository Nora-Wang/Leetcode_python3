Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

    
# Version 1: merge two sorted array
# time: O(n + m), space: O(n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_record = list(nums1[:m])
        
        i, j, = 0, 0
        index = 0
        while i < m and j < n:
            if nums1_record[i] < nums2[j]:
                nums1[index] = nums1_record[i]
                i += 1
            else:
                nums1[index] = nums2[j]
                j += 1
            
            index += 1
            
        while i < m:
            nums1[index] = nums1_record[i]
            i += 1
            index += 1
        while j < n:
            nums1[index] = nums2[j]
            j += 1
            index += 1
        
        return
    
# Optimal
# time: O(n + m), space: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        index = n + m - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[index] = nums2[j]
                j -= 1
            else:
                nums1[index] = nums1[i]
                i -= 1
            index -= 1
                
        while j >= 0:
            nums1[index] = nums2[j]
            index -= 1
            j -= 1
        
        return
    
    
    

双指针

code:
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1
        
        #这里不能简写为
        #if j >= 0:
        #nums1[:j] = nums2[:j]
        #因为有一个case:nums1 = [0], m = 0, nums2 = [1], n = 1
        #我也不理解为啥m为0...但确实如果用上面的跑,j会等于0,这样后面的nums1[:j]就取不到值
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        
        return nums1
        
