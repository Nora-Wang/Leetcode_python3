Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.


#time: O(n), space: (n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        stack = []
        l = len(nums)
        res = [-1] * l
        
        for i in range(l * 2):
            while stack and nums[stack[-1] % l] < nums[i % l]:
                if res[stack[-1] % l] == -1:
                    res[stack[-1] % l] = nums[i % l]
                stack.pop()
            
            stack.append(i)
        
        return res
    
    
#time: O(n), space: O(n)    
单调栈问题
因为是环形,直接nums = nums + nums即可,result取前半部
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nums = nums + nums
        results = [-1] * len(nums)
        
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                results[stack[-1]] = nums[i]
                
                stack.pop()
        
            stack.append(i)
        
        return results[:len(results) // 2]
