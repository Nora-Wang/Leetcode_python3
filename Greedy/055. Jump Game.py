Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
             
             
code:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        longest = 0
        
        #找每一位的最远距离
        for i in range(len(nums)):
            #如果当前位的index小于目前可达到的最远距离，那就是达不到该点，返回F 
            #eg:[3,2,1,0,4]
            if i > longest:
                return False
            
            #更新当前最远距离
            longest = max(longest, nums[i] + i)
            
        return True
        
        
