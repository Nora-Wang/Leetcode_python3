Given an integer array, find the top k largest numbers in it.

Example

Example1

Input: [3, 10, 1000, -99, 4, 100] and k = 3
Output: [1000, 100, 10]
Example2

Input: [8, 7, 6, 5, 4, 3, 2, 1] and k = 5
Output: [8, 7, 6, 5, 4]


code:
时间O(nlogn)
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        if not nums:
            return []
            
        sorted_nums = sorted(nums, reverse = True)
        
        result = []
        for i in range(k):
            result.append(sorted_nums[i])
        return result
