Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]


DFS模板问题

code:
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        
        #这里的start是从2开始的,所以后续只要temp中有值,temp+remain即可被加入result
        self.dfs(n, [], 2, result)
        
        return result
    
    def dfs(self, remain, temp, start, result):
        #当temp中有值时,直接将temp与remain组合即为result之一
        if len(temp):
            result.append(temp + [remain])
        
        #这里的取值很巧妙,取的是[start, int(math.sqrt(remain))],这样可以减少完美的剪枝
        for i in range(start, int(math.sqrt(remain)) + 1):
            #当不能作为因子时,则直接跳过
            if remain % i != 0:
                continue
                
            temp.append(i)
            #注意对remain和start的取值处理
            self.dfs(remain / i, temp, i, result)
            temp.pop()
