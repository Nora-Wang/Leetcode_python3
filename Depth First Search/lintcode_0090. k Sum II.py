Given n unique postive integers, number k (1<=k<=n) and target.

Find all possible k integers where their sum is target.

Example

Example 1:

Input: [1,2,3,4], k = 2, target = 5
Output:  [[1,4],[2,3]]
Example 2:

Input: [1,3,4,6], k = 3, target = 8
Output:  [[1,3,4]]



code:
class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: target: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        results = []
        self.dfs(A, 0, [], k, target, results)
        
        return results
        
    def dfs(self, nums, start_index, temp, k, cur_target, results):
        if k == 0 and cur_target == 0:
            results.append(list(temp))
            return
        
        if k <= 0 or cur_target <= 0:
            return
        
        for i in range(start_index, len(nums)):
            temp.append(nums[i])
            self.dfs(nums, i + 1, temp, k - 1, cur_target - nums[i], results)
            temp.pop()
