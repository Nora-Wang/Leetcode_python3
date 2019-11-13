Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]



code:
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
         #定义一个用过的集合visited
         #注意visited的写法:要建立一个长度为len(nums),值都为False的list
        visited = [False] * len(nums)
            
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
            #注意后续需要将visited[0]从新设置为False,因为到后面先将2加入temp时,这时的1应该在备选数据中,而不应在visited中
            if visited[i]:
                continue
                
            #去重
            #当前数和前面的数一样,并且前面没有被用过
            #not visited[i - 1]设计的很精妙
            #eg:对于[1,2',2'']来说,当第一个值取[1]时,存在一种情况[1,2',2''],此时相当于先访问的[1,2'],2'的visited=True(因为它已经被加入temp)
            #而当[1,2']的情况都分析后,[1,2'']应该被跳过(与[1,2']结果一样):2'==2'',并且此时2'的visited=False(因为2'并没有被加入temp)
            if i and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue
                
                
            #后面的这些部分呈镜像对称
            temp.append(nums[i])
            #用的时候设置为True:[]->[1]
            visited[i] = True
            self.dfs(nums, visited, temp, results)
            #用完了需要返回False:[1]->[]
            visited[i] = False
            temp.pop()
