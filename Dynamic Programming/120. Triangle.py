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

     
#自顶向下的动态规划 Version
状态:坐标, 方程:从哪儿来, 初始化:起点, 答案:终点
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        
        #state: dp[i][j]代表从i,j走到最底层的最短路径值
        #建立初始化三角矩阵
        dp = [[0] * (i + 1) for i in range(n)]
        
        #initialize: 初始化最左边的一斜列和最右边的一斜列,因为它们没有左上角和右上角的点
        #初始化第0行
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            #每个值都是上面的结果加上当前位置的值 
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            #每个值都是左上的结果加上当前位置的值 
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        
        #由于前面计算两侧时已经将第1行计算完了,因此直接从第2行开始计算
        for i in range(2, n):
            for j in range(1, i):
                #该点的左上和右上的最小path sum值+自己本身的值 = 该点的最小path sum
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                
        #answer: 最后一排的最小值
        return min(dp[n - 1])

     
     
#自底向上的动态规划
状态:坐标, 方程:到哪儿去, 初始化:终点, 答案:起点
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        #state: dp[i][j]代表从i,j走到最底层的最短路径值
        dp = [[0] * (i + 1) for i in range(n)]
        
        #initialize: 初始化终点(最后一层)
        for i in range(n):
            dp[-1][i] = triangle[-1][i]
            
        #function:从下往上倒过来推导,计算每个坐标到哪儿去
        for i in range(n-2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        
        #answer: 起点就是答案
        return dp[0][0]
