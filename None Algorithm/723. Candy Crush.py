This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.

 

Example:

Input: board =  [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]  Output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]  Explanation:   
 

Note:

The length of board will be in the range [3, 50].
The length of board[i] will be in the range [3, 50].
Each board[i][j] will initially start as an integer in the range [1, 2000].



# 并没有AC
# time: O((r * c)^2), space: O(1)
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not len(board) or not len(board[0]):
            return []
        
        row, col = len(board), len(board[0])
        # varify is there still have candy need to crush
        stop = True
        
        # find the four direction range
        for i in range(row):
            for j in range(col):
                # edge case
                if board[i][j] == 0:
                    continue
                    
                left, right, up, down = j - 1, j + 1, i - 1, i + 1
                center = abs(board[i][j])
                
                while left >= 0 and board[i][left] == center:
                    left -= 1
                while right < col and board[i][right] == center:
                    right += 1
                while up >= 0 and board[up][j] == center:
                    up -= 1
                while down < row and board[down][j] == center:
                    down += 1
                
                # get distance
                l_r = right - left - 1
                u_d = down - up - 1
                
                if l_r >= 3:
                    stop = False
                    for index in range(left + 1, right):
                        board[i][index] = -abs(board[i][index])
                
                if u_d >= 3:
                    stop = False
                    for index in range(up + 1, down):
                        board[index][j] = -abs(board[index][j])
        
        # renew borad
        # 3, -1, -1, -1, -1, 4,1,411
        for j in range(col):
            slow, fast = row - 1, row - 1
            while fast >= 0:
                while fast >= 0 and board[fast][j] <= 0:
                    fast -= 1

                if fast >= 0:
                    board[slow][j], board[fast][j] = board[fast][j], board[slow][j]
                    fast -= 1
                    slow -= 1

            for i in range(slow, -1, -1):
                board[i][j] = 0
                
        return board if stop else self.candyCrush(board)
