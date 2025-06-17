Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

# 2025/6/17
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        self.helper(nums, set(), [], res)

        return res

    def helper(self, nums, visited, temp, res):
        if len(temp) == len(nums):
            res.append((list(temp)))
            return

        for i in range(len(nums)):
            if i in visited:
                continue

            # 这里的逻辑是，如果nums[i]的值与nums[i-1]一样，并且nums[i-1]已经在visited里面了，
            # 那就说明在当前这个level的recursion里，没必要再往下走了，因为同样value的recursion，及同样temp的结果已经在nums[i-1]那一层里生成过了
            if i > 0 and nums[i] == nums[i - 1] and (i - 1) in visited:
                continue
            
            visited.add(i)
            temp.append(nums[i])
            self.helper(nums, visited, temp, res)
            temp.pop()
            visited.remove(i)
    
        return



# 10/14/2020
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        res = []
        nums.sort()
        self.dfs(nums, set(), [], res)
        
        return res
    
    def dfs(self, nums, visited, temp, res):
        if len(temp) == len(nums):
            res.append(list(temp))
            return
        
        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1] and ((i - 1) not in visited):
                continue
                
            if i in visited:
                continue
            
            visited.add(i)
            temp.append(nums[i])
            self.dfs(nums, visited, temp, res)
            temp.pop()
            visited.remove(i)
            






!!!!!!!!!!!!!!!!
注意区别两种不同的去重情况
[1,2',2'']
第一种visited是去除选取数据的不同:在为temp加入数据时,2'和2''都能被加到temp中[1,2',2''],但都不能被加入两次[1,2'',2'']or[1,2',2']
第二种i > start_index and nums[i] == nums[i - 1]是防止重复情况的出现:[1,2']被分析后,[1,2'']就不用分析了,因为结果是一样的




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
            #去重 1
            #用过了(当前temp里正在用)就跳过
            #对于[1,2,3],当1被加入进了temp,则visited[0]=True;temp后续加第二个值时,就只能在剩余的数(2,3)里面选
            #注意后续需要将visited[0]从新设置为False,因为到后面先将2加入temp时,这时的1应该在备选数据中,而不应在visited中
            if visited[i]:
                continue
                
            #去重 2
            #相当于if i > start_index and nums[i] == nums[i - 1]
            #这道题因为没有start_index,因此用not visited[i - 1]代替          
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
