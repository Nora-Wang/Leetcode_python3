Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:

Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:

The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].


类似题目：
611. Valid Triangle Number
lintcode_0609. Two Sum - Less than or equal to target
lintcode_0443. Two Sum - Greater than target



思路：
使用Two Pointer
先sort，然后for循环最大边的位置 i，接下来的任务就是在 0~i-1 之间用Two Sum的方法找到 > S[i]的组合(因为另外两个边的值都必须要小于i的值)

code:
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort(reverse=True)
        result = 0
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                value = nums[left] + nums[right]
                
                if value > nums[i]:
                    result += right - left
                    left += 1
                else:
                    right -= 1
        
        return result
