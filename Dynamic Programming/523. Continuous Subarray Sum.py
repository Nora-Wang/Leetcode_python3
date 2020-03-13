Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.


code:
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #corner case
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1] == 0:
                    return True
            return False
        
        #对每个值都从头到尾的遍历一遍,这里要记录上一次的sum,这样每次只用加当前num[j]即可
        for j in range(1, len(nums)):
            i = 0
            while i < j:
                nums[i] = nums[i] + nums[j]

                if nums[i] % k == 0:
                    return True

                i += 1
            
        
        return False
