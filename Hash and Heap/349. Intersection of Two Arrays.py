Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.


# 1. two set
# time: O(n + m), space: O(n + m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        res = set()
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        if len(nums1) < len(nums2):
            shorter_set = nums1
            nums = nums2
        else:
            shorter_set = nums2
            nums = nums1
        
        for num in nums:
            if num in shorter_set:
                res.add(num)
        
        return list(res)
        
# 2. Built-in Set Intersection
# time: O(n + m), space: O(n + m)        
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
        
# 3. brute force
# time: O(n * len(res) * m), space: O(1)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        
        for num in nums1:
            if num not in res and num in nums2:
                res.append(num)
        
        return res
        
        
# 4. two pointer
# FB interview
# time: O(n + m), space: O(1), ignor the sort part
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        
        nums1.sort()
        nums2.sort()
        
        p1, p2 = 0, 0
        res = []
        
        while p1 < len(nums1) and p2 < len(nums2):
            while p1 + 1 < len(nums1) and nums1[p1] == nums1[p1 + 1]:
                p1 += 1
            while p2 + 1 < len(nums2) and nums2[p2] == nums2[p2 + 1]:
                p2 += 1
                
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        
        return res
        
        
