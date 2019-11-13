Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

code:
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #尽量少的使用全局变量
        combinations = []
        
        #if not nums:
        #   return combinations
        #为什么不做边界条件判断？随课教程里是有判断nums == null的。为什么用python的时候加上 if not nums: return results会挂掉呢？
        #因为nums = []的时候如果target = 0的话,存在且仅存在一种方案,即结果应为return [[]];但是如果target != 0,结果就应该是return []
        #其边界nums = []的情况会随着target为不为0而变化，因此不能直接设置边界情况

        self.dfs(nums, 0, [], combinations)
        
        return combinations
    
    def dfs(self, nums, index, temp, combinations):
        #这里为什么需要写成list(temp), temp本身不就是list吗? 
        #这里牵扯到一个copy问题，如果不加list，那么copy的就是temp的reference，因此list之后的改变都会导致之前加入值的改变，
        #加上list()之后就是建立了一个当前temp的copy，之后无论list如何改变，就不变了
        combinations.append(list(temp))
        
        for i in range(index, len(nums)):
            temp.append(nums[i])
            self.dfs(nums, i + 1, temp, combinations)
            temp.pop()
