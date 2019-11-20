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

时间复杂度:
O(s * n^2)


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
    #step 1 递归定义: 需要用一个temp来记录每次符合条件的结果,用results来记录所有的结果
    def dfs(self, n, temp, results):
    
    #step 2 递归出口: 当temp的长度与n相等,即符合题目要求(对于n*n的矩阵来说,被成功放入了n个Q);对于n = 2或者n = 3来说,只能被放入n - 1个Q
        if len(temp) == n:
            results.append(self.draw(temp))
    
    #step 3 递归解析: 对于每一行(temp的index)来说,判断应该在哪一列(col)加入Q,若不是该列,则col += 1
                     #temp.append(col)中 temp[row] = col
    #分析过程:
    #1.判断第a行,能在第0列加入Q,则temp[a] = 0,继续dfs
    #2.判断第b行,因为第0列在temp中,所以self.is_valid为False,continue;
    #  因为第1列与temp[a] = 0的斜率的绝对值为1,所以self.is_valid为False,continue;
    #  因为第2列不在temp中,且与temp[a] = 0的斜率的绝对值不为1,所以self.is_valid为True,可以加入temp,即temp[b] = 2
    
    #当把temp[a] = 0的情况都判断结束后,通过backtracking将temp全部pop出,
    #然后进行第一层(即第a行)for循环的第二个值(col++,即第1列),即temp[a] = 1的情况
        for col in range(n):
            if not self.is_valid(col, temp):
                continue
            temp.append(col)
            self.dfs(n, temp, results)
            temp.pop()
    
    #画出棋盘
    #此时len(temp) = n
    def draw(self, temp):
        out = []
        #对于每一行来说,先建立一个长度为n的全为'.'的矩阵draw_every_row,代表第row行来说有n个'.'
        #由于temp[row] = col,即对于第row行来说,它的第temp[row]列的值应为'Q'
        for row in range(len(temp)):
            draw_every_row = ['.'] * len(temp)
            draw_every_row[temp[row]] = 'Q'
            #最后将draw_every_row转换为str
            out.append(''.join(draw_every_row))
            
        return out
    
    #判断对于目前的temp来说,是否可以在第len(temp)行的第col列加入'Q',不行就dfs函数col+=1,然后再做判断
    #这里相当于给出一个定点(len(temp), col),判断是否与之前存入temp的点位于同一列or斜率绝对值为1(即在一条直线上)
    #行=len(temp)是因为行相当于temp的index,其取值从a开始,因此len(temp)相当于取到目前temp的下一行
    def is_valid(self, col, temp):
        #去重
        #行:因为temp的index代表行,每次都是往temp的下一个index加入值(即第len(temp)行),因此行肯定不会重复
        #列:当col在temp中,即表示之前行的某个点已经被放入该列了(该列不能再被放入Q),则对于第len(temp)行不能再将Q放入第col列了
        if col in temp:
            return False
        
        #斜对角:即for循环中if部分的比较
        #对于之前已经被放入temp的点来说,若用于判断给出的定点(len(temp), col)与之前的temp中的点在不在一条斜线上,若不在则该定点可用
        for row in range(len(temp)):
            #其实就是用已经存在于temp中的点(x1,y1)和即将被放入的点(x2,y2)作比较，确保斜率(y2-y1)/(x2-x1)的绝对值为1或者-1
            #(x1,y1)=(row, temp[row]), (x2,y2)=(len(temp), col) -> abs(col - temp[row]) == abs(len(temp) - row))
            if abs(col - temp[row]) == abs(len(temp) - row)):
                return False
            
        return True
            
