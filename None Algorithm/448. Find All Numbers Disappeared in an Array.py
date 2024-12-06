Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# time O(n), space O(n)
# set
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setNums = set(nums)
        res = []
        
        for num in range(1, len(nums) + 1):
            if num not in setNums:
                res.append(num)
        
        return res


# extra array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mark = [0] * n
        
        for num in nums:
            mark[num - 1] = num
        
        res = []
        for i in range(n):
            if mark[i] == 0:
                res.append(i + 1)
        
        return res

# time O(n), space O(1)
# no extra space
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        
        return res
        
