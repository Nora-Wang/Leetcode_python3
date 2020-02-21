Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
Note:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].




code:
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #用hash_map记录每一个curt_sum出现的次数
        hash_map = {}
        
        curt_sum = 0
        count = 0
        
        for i in range(len(nums)):
            curt_sum += nums[i]
            
            #当curt_sum - k 出现在HashMap中，叠加count 
            if curt_sum - k in hash_map:
                count += hash_map[curt_sum - k]
            
            hash_map[curt_sum] = hash_map.get(curt_sum, 0) + 1
        
        #因为之前算的count都是curt_sum - k的值,即只取nums的中间一截,而这里的k则是从头到尾加起来为k的情况,这得另加
        if k in hash_map:
            count += hash_map[k]
            
        return count
            
