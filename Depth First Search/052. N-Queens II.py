The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]


实际是N-queens I的简化版，省去了返回所有解决方案的麻烦，直接用一个全局变量self.count计算已经找到的解决方案的个数就搞定了

Question:
在主函数里令self.count = 0,之后在dfs函数中满足条件就加一(就是如下代码写法),可以AC,
然而如果在主函数中令count = 0,然后把count传入dfs函数中,每次满足条件就加一,最后答案却一直都是0

Answer:
Python 里面函数参数是引用类型，也就是对象。所以你直接放一个数字进去python会把数字作为按值传递处理，返回的时候参数永远不会被函数内部改变，
假如你把那个ans = 0 放进一个只有一个元素list的或者嵌入到一个新对象传就没事


code:
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        self.dfs(n, [])
        
        return self.count
    
    def dfs(self, n, temp):
        if len(temp) == n:
            self.count += 1
            
        for row in range(n):
            if not self.check(row, temp):
                continue
                
            temp.append(row)
            self.dfs(n, temp)
            temp.pop()
            
    def check(self, row, temp):
        cur_col = len(temp)
        for col in range(cur_col):
            if row == temp[col] or abs(row - temp[col]) == abs(cur_col - col):
                return False
            
        return True
