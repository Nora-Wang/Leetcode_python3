Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]


时间复杂度: O(2^n)
空间复杂度: O(n)


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
            
        results = []
        candidates.sort()
        
        self.dfs(candidates, 0, [], results, target)
        
        return results
        
    #递归的定义
    def dfs(self, candidates, start_index, temp, results, cur_target):
        #递归的出口
        if cur_target < 0:
            return
        if cur_target == 0:
            results.append(list(temp))
            
        #递归的拆解
        for i in range(start_index, len(candidates)):
            #去重
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue
            
            temp.append(candidates[i])
#与Combination sum I的区别是,这里为i+1,因为题目多了一个要求:Each number in candidates may only be used once in the combination.
            self.dfs(candidates, i + 1, temp, results, cur_target - candidates[i])
            temp.pop()

