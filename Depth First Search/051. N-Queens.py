The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.



因为要求输出所有情况,肯定是一道dfs的题目,具体分析:

首先明确queen的性质，她可以杀与其同在一条直线上的其他棋子（Any two queens can't be in the same row, column, diagonal line），
而我们要在 N*N 大小的棋盘中放入 N 个 queen('Q')，所以我们一定是每个 row 放一个 queen,即dfs中的for循环的作用
然后，具体地，我们对每一个 row，考虑其上每个 col 位置放 queen 的话会不会影响之前放置好的第 0 to row-1 row 上的queen。
如果当前 (row, col) 可以，就继续向 row + 1 继续 dfs。




code:
class Solution(object):
    #main函数,可判断一下n是否>=0
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n:
            return []
        
        results = []
        self.dfs(n, [], results)
        
        return results
    
    #dfs递归模板
    #step 1 递归定义: 需要用一个subset来记录每次符合条件的结果,用results来记录所有的结果
    def dfs(self, n, subset, results):
    
    #step 2 递归出口: 当subset的长度与n相等,即对于n*n的矩阵来说,被成功放入了n个Q
        if len(subset) == n:
            results.append(self.drew(subset))
    
    #step 3 递归解析: 对于每一列(subset的index)来说,判断应该在哪一行(row)加入Q,若不是该行,则row+=1
                     #subset.append(row)中 subset[col] = row
        for row in range(n):
            if not self.check(row, subset):
                continue
            subset.append(row)
            self.dfs(n, subset, results)
            subset.pop()
    
    #画出棋盘
    def drew(self, subset):
        out = []
        #由于是一个n*n的矩阵,行数和列数都是len(subset)=n
        len_row, len_col = len(subset), len(subset)
        
        #对于每一列来说,先建立一个长度为len_row的全为'.'的矩阵temp,代表第col列来说有len_row行个'.'
        #由于subset[col] = row,即对于第col列来说,它的第subset[col]行的值应为'Q',
        #最后将temp转换为str
        for col in range(len_col):
            temp = ['.'] * len_row
            temp[subset[col]] = 'Q'
            out.append(''.join(temp))
            
        return out
    
    #判断对于目前的subset来说,是否可以在第len(subset)+1列的第row行加入'Q'(参考subset.append(row),即向subset的下一个index赋值为row,因此列不会重复),
    #不行就dfs函数row+=1,然后再做判断
    def check(self, row, subset):
        len_cur_col = len(subset)
        for col in range(len_cur_col):
            #列:因为subset的index代表列,每次都是往subset的下一个index加入值,因此列肯定不会重复
            #行:将dfs for循环得到的row和subset中已经存入的row做比较,判断是否该row已经被使用
            #斜对角:即or后半部分的比较
            #其实就是用已经确定可以放置的点(x1,y1)和将要放置的点(x2,y2)作比较，确保斜率(y2-y1)/(x2-x1)的绝对值为1或者-1
            #abs(y2-y1) == abs(x2-x1), x1, y1 表示已经确定的点的横坐标和纵坐标，x2, y2表示将要确定的那个点的横坐标和纵坐标
            #(x1,y1)=(col, subset[col]), (x2,y2)=(cur_col,row) -> abs(row - subset[col]) == abs(cur_col - col)
            if subset[col] == row or abs(row - subset[col]) == abs(len_cur_col - col):
                return False
            
        return True
            
