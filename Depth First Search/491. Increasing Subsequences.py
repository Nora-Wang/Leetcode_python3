Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

 

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
 

Note:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.


DFS题型,但是剪枝部分不好想到
想着那棵树:利用visited来记录竖着的部分,若有重复则continue;横着延伸的部分则是与temp的最后一个值比较,不能与nums[i-1]比较,因为这道题不能sort
(理由:降序的没有结果.eg:[4,3,2,1],return []),因此用nums[i] >= temp[-1]来判断是否为升序


code:
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        combinations = []
        
        self.dfs(nums, 0, [], combinations)
        
        return combinations
    
    def dfs(self, nums, start_index, temp, combinations):
        if len(temp) > 1:
            combinations.append(list(temp))
        
        # 这题因为array不是sorted的，也不能sort，因此这里使用visited来避免在同层中选到重复的num
        visited = set()
        
        for i in range(start_index, len(nums)):
            # 避免出现[4,7], [4,7]的情况
            # 等同sorted的nums中 if i > start_index and nums[i] == nums[i - 1]
            if nums[i] in visited:
                continue
            
            visited.add(nums[i])
            
            if not temp or nums[i] >= temp[-1]:
                temp.append(nums[i])
                self.dfs(nums, i+1, temp, combinations)
                temp.pop()
            
