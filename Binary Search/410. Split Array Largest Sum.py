Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.


与copy book/wood cut同类型

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end = max(nums), sum(nums)
        
        while start + 1 < end:
            mid = (end + start) // 2
            
            if self.check(mid, nums) <= m:
                end = mid
            else:
                start = mid
        
        if self.check(start, nums) <= m:
            return start
        return end
    
    def check(self, mid, nums):
        count = 0
        curt_sum = 0
        
        for i in range(len(nums)):
            if curt_sum + nums[i] > mid:
                count += 1
                curt_sum = 0
                
            curt_sum += nums[i]
        
        return count + 1 if curt_sum > 0 else count
            
            
                
