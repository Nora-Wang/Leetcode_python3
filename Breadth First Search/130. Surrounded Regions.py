Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.


BFS题目
思路:对regions的所有边缘nodes进行bfs,将为O的标记为M,最后遍历一遍board,当为M则赋为O,否则一定为X

code:
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #corner case:对于二维数组,一定要注意board[0]
        if not board or not board[0]:
            return []
        
        n, m = len(board), len(board[0])
        
        #对于处于第一列和最后一列的边缘nodes
        for i in range(n):
            self.bfs(board, i, 0)
            self.bfs(board, i, m - 1)
        
        #对于处于第一行和最后一行的边缘nodes
        for j in range(m):
            self.bfs(board, 0, j)
            self.bfs(board, n - 1, j)
        
        #除了值为M的,其余都应为X
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                
        return board
    
    #对每个为O的node进行bfs搜索,将该node周围的O都变为M
    def bfs(self, board, i, j):
        if board[i][j] == 'X':
            return
        board[i][j] = 'M'
        
        node = [i, j]
        queue = collections.deque([node])
        
        while queue:
            node = queue.popleft()
            for direct in DIRECTIONS:
                new_i = node[0] + direct[0]
                new_j = node[1] + direct[1]
                if self.is_valid(board, new_i, new_j):
                    board[new_i][new_j] = 'M'
                    new_node = [new_i, new_j]
                    queue.append(new_node)
    
    #判断该node是否在范围内,且值为O
    def is_valid(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
            return True
        return False
        
        #或者
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if board[i][j] != 'O':
            return False
        
        return True
