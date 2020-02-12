Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]


思路:
对于每个a[i]，我们将其对应的a[a[i]−1]取相反数，如果已经为负数则将a[i]加入答案中


code:
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        result = []
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                result.append(abs(nums[i]))
            else:
                nums[index] *= -1
            
        return result
            
            
        
        
