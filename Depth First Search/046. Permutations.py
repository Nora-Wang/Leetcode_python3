Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]



DFS模板
注意一下递归出口


code:
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        #定义一个用过的集合visited
        visited = set()
            
        self.dfs(nums, visited, [], results)
        
        return results
   
    #1. 递归的定义
    #找到所有temp开头的排列,加到results里
    def dfs(self, nums, visited, temp, results):
      
    #2. 递归出口:temp的长度
        #因为需要将所有的nums都排序
        if len(nums) == len(temp):
            results.append(list(temp))
    
    #3. 递归的拆解
        for i in range(len(nums)):
            #去重
            #用过了(当前temp里正在用)就跳过
            #对于[1,2,3],当1被加入进了temp,则visited[0]=True;temp后续加第二个值时,就只能在剩余的数(2,3)里面选
            if nums[i] in visited:
                continue
                
            #后面的这些部分呈镜像对称
            temp.append(nums[i])
            #用的时候将其加入visited
            visited.add(nums[i])
            self.dfs(nums, visited, temp, results)
            #用完了需要返回
            visited.remove(nums[i])
            temp.pop()
