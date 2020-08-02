Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

# 80/01/2020
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        self.dfs(candidates, 0, [], target, res)
        
        return res
    
    def dfs(self, candidates, index, temp, curt_target, res):
        if curt_target == 0:
            res.append(list(temp))
            return
        
        if curt_target < 0:
            return
        
        for i in range(index, len(candidates)):
            temp.append(candidates[i])
            self.dfs(candidates, i, temp, curt_target - candidates[i], res)
            temp.pop()



与Subsets比较:
• Combination Sum限制了组合中的数之和:加入一个新的参数cur_target来限制
• Subsets无重复元素,Combination SumII有重复元素:需要先去重
• Subsets一个数只能选一次,Combination Sum一个数可以选很多次:搜索时从 start_index 开始而不是从 start_index + 1

  
时间复杂度:
T(n) = O(s * n) (s是一共有多少个solution,s<=2^n)

code:
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #这次可以写if not nums是因为最后结果不存在[[]]的情况了,当没有结果时,其返回值就应该为[]
        if not candidates:
            return []
        
        results = []
        
        self.dfs(candidates, 0, [], results, target)
        
        return results
    
    #递归的定义
    def dfs(self, candidates, start_index, temp, results, cur_target):
        #递归的出口
        #建议都写上return
        #注意这里一定要写<0的情况,因为cur_target在每次减去值后,其结果不止是=0的情况,还可能<0(这一情况因为无法满足要求,必须舍弃)
        if cur_target < 0:
            return
        if cur_target == 0:
            return results.append(list(temp))
        
        #注意这里的起始值为start_index
        for i in range(start_index, len(candidates)):
            temp.append(candidates[i])
            #这里要是i,而不是i+1,因为在得到target的过程中,数据可以重复;eg example 2中的[2,2,2,2]
            #题目中的:The same repeated number may be chosen from candidates unlimited number of times.
            self.dfs(candidates, i, temp, results, cur_target - candidates[i])
            temp.pop()
