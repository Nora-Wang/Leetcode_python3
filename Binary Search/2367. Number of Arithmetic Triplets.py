You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.

 

Example 1:

Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
Example 2:

Input: nums = [4,5,6,7,8,9], diff = 2
Output: 2
Explanation:
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.
 

Constraints:

3 <= nums.length <= 200
0 <= nums[i] <= 200
1 <= diff <= 50
nums is strictly increasing.



# brute force
# Time O(n^3), Space O(1)
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[j] - nums[i] == nums[k] - nums[j] == diff:
                        count += 1
        
        return count



# Array
# Time O(n^2), Space O(1)
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n - 2):
            if (nums[i] + diff) in nums and (nums[i] + diff * 2) in nums:
                count += 1
        
        return count



# Hash Set
# Time O(n), Space O(n)
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        n = len(nums)
        set_nums = set(nums)

        for i in range(n - 2):
            if (nums[i] + diff) in set_nums and (nums[i] + diff * 2) in set_nums:
                count += 1
        
        return count


# Binary Search
# Time O(n * logn), Space O(1)
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        n = len(nums)
        set_nums = set(nums)

        for i in range(n - 2):
            if self.binary_search(nums, i, n - 1, nums[i] + diff) and self.binary_search(nums, i, n - 1, nums[i] + diff * 2):
                count += 1
        
        return count

    def binary_search(self, nums, left, right, target):
        if left > right:
            return False

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            if nums[mid] < target:
                left = mid
            else:
                right = mid

        return nums[left] == target or nums[right] == target
