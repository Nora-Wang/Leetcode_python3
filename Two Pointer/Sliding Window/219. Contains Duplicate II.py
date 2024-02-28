Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

# Time O(n), Space O(k)

# 丑陋的代码
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = set()
        if k >= len(nums):
            for num in nums:
                if num in record:
                    return True
                record.add(num)
            return False
        
        for num in nums[:k+1]:
            if num in record:
                return True
            record.add(num)
        
        for i in range(k + 1, len(nums)):
            record.remove(nums[i-k-1])
            if nums[i] in record:
                return True
            record.add(nums[i])
        
        return False

# 优雅的代码
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = set()
        
        for i in range(len(nums)):
            if i > k:
                record.remove(nums[i - k - 1])
            
            if nums[i] in record:
                return True
            
            record.add(nums[i])
        
        return False
