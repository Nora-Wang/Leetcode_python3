Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.



DP最典型的记忆化搜索memoization search:
在DFS的基础上,使用一个hash表记录之前计算过的数据,避免重复计算


直接使用dfs,时间复杂度为O(2^n)
使用dp后,时间复杂度为O(n),只用遍历所有nodes

code:
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #用一个hash表记录之前走过的nodes的最小和
        return self.dc(triangle, 0, 0, {})
    
    def dc(self, triangle, x, y, visited):
        #当超过最后一层后，结果返回0
        if x == len(triangle):
            return 0
        
        #记忆化搜索，如果在memo中，可以直接返回memo中的值 
        if (x,y) in visited:
            return visited[(x,y)]
        
        #分治，分别向下和向右下递归
        left = self.dc(triangle, x + 1, y, visited)
        right = self.dc(triangle, x + 1, y + 1, visited)
        
        #记录当前点的值
        visited[(x,y)] = min(left, right) + triangle[x][y]
        
        return min(left, right) + triangle[x][y]
