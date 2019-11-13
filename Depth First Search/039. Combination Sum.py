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
        #当后续需要将candidates[i]与candidates[i - 1]做比较时,一定要记得sort
        candidates.sort()
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
            #去重
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue
                
            temp.append(candidates[i])
            cur_target -= candidates[i]
            #这里要是i,而不是i+1,因为在得到target的过程中,数据可以重复;eg example 2中的[2,2,2,2]
            self.dfs(candidates, i, temp, results, cur_target)
            cur_target += candidates[i]
            temp.pop()
            

            
Summary:
    
1. combination模板:
    def comnination(self, candidates, target):
        results = [] #定义结果
        candidates.sort()
        self.dfs(candidates, 0, temp, results, target) 
        return results
    #recursion definition     
    def dfs(self, candidates, start_index, temp, results, cur_target): 
        #recursion end case
        if cur_target < 0:
            return
        if cur_target == 0: 
            return results.append(list(temp))

        #recursion explanation
        #镜像对称
        for i in range(start_index, len(candidates)): 
            temp.append(candidates[i])#元素写入temp 
            cur_target -= candidates[i]
            self.dfs(candidates, i, temp, results, cur_target) 
            cur_target += candidates[i]
            temp.pop()#弹出元素（因为用过了） 
 
2. 组合的几个关键问题:
2.1 起始索引i在递归函数dfs中怎么变化？ 
i=i，一个元素可以被多次使用 
i=i+1;一个元素只能被用一次 
dfs(candidates, temp, remainder - candidates[i], 1+1)
2.2 dfs如何移除最后一个元素？ 
temp.pop()
2.3 假如数组中包含多个相同的元素，但是这些元素每个只能选一次，并且结果中不能出现相同的组合，怎么办？ 
if i > startIndex and nums[i] == nums[i - 1]:
    continue
 
 
3. combinations要在在1-n的范围内选择k个数时,想明白以下几点： 
3.1 搜索的起始位置是什么（是start_index还是0？） 
3.2 搜索的终点是什么？（是<=还是<?) 
3.3 搜索的出口是什么？（是否满足了所有的限制条件？） 
3.4 无效的答案是否提前进行了剪枝？(建议在每个确定无效或有效的solution都添加return)


