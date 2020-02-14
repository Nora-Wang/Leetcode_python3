According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?



code:
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        
        #当死细胞周围正好有 3 个活细胞时，则满足第三种状态，所以需要重新赋值：board[i][j] = 2
        #当活细胞周围正好有 < 2 个或者 > 3 个活细胞时，则满足第四种状态，所以需要重新赋值：board[i][j] = 3
        for i in range(n):
            for j in range(m):
                count = self.check(board, i, j)
                if board[i][j] == 0 and count == 3:
                    board[i][j] = 2
                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = 3
        
        #遍历一遍所有数字,是2/3的情况更改为对应的1/0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0
        
        return
    
    
    def check(self, board, x, y):
        count = 0
        for direct in DIRECTIONS:
            x_ = x + direct[0]
            y_ = y + direct[1]
            
            if self.is_valid(x_, y_, board):
                count += 1
        
        return count
            
    
    def is_valid(self, x, y, board):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        
        #2的时候也是0
        if board[x][y] == 0 or board[x][y] == 2:
            return False
        
        return True
