Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

模板DFS

code:

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #！！！要记得sort！
        #为后续的去重提供nums[i] == nums[i - 1]条件
        nums.sort()
        combinations = []
        self.dfs(nums, 0, [], combinations)
        
        return combinations
    
    def dfs(self, nums, start_index, temp, combinations):
        combinations.append(list(temp))
        
        for i in range(start_index, len(nums)):
      #去重
      #解释:
            #对于2'和2''来说
            #第一步:当i = start_index时，访问nums[i] = 2'
            #第二步:然后i++
            #第三步:当i = start_index + 1 > start_index时,访问nums[i] = 2'';此时nums[i - 1] = 2'
            #因此当判断出i > start_index并且nums[i] == nums[i - 1]时应当跳过
      #nums[i - 1]一定存在,不需要特殊判断i > 0
            #因为start_index最小值为0,而i > start_index,因此i的最小值为1
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            
            temp.append(nums[i])
            self.dfs(nums, i + 1, temp, combinations)
            temp.pop()
