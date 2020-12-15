Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


# brute force
# time: O(nlogn), space: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums])
        
        
# two pointer
# time: O(n), space: O(1)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # negative | positive
        positive = 0
        while positive < len(nums) and nums[positive] < 0:
            positive += 1
        
        # compare
        res = []
        negative = positive - 1
        while negative >= 0 and positive < len(nums):
            if abs(nums[negative]) < abs(nums[positive]):
                res.append(nums[negative]**2)
                negative -= 1
            else:
                res.append(nums[positive]**2)
                positive += 1
        
        # add the rest part
        while negative >= 0:
            res.append(nums[negative]**2)
            negative -= 1
        while positive < len(nums):
            res.append(nums[positive]**2)
            positive += 1
        
        return res
