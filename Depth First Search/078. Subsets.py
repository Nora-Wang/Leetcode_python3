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


标准DFS模板

code:
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #当nums为空时,它还有个子集即空集，所以它的subsets应该是[[]]
        #这是特殊情况
        #这个判断可以不写
        if not nums:
            return [[]]
        
        #尽量少的使用全局变量
        combinations = []

        self.dfs(nums, 0, [], combinations)
        
        return combinations
    
    def dfs(self, nums, index, temp, combinations):
        #这里为什么需要写成list(temp), temp本身不就是list吗? 
        #这里牵扯到一个copy问题，如果不加list，那么copy的就是temp的reference，因此list之后的改变都会导致之前加入值的改变，
        #加上list()之后就是建立了一个当前temp的copy，之后无论list如何改变，就不变了
        #这新建了一个list，list的构造接受一个Iterable对象作为参数，并将该对象内的元素按顺序添加到新建的list中。这也是一次Deep Copy。
        combinations.append(list(temp))
        
        for i in range(index, len(nums)):
            temp.append(nums[i])
            self.dfs(nums, i + 1, temp, combinations)
            temp.pop()
