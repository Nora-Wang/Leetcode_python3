Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.


# 11/02/2020
'''
clarification
1. 9 * 9 board with only 1 ~ 9 digits
2. rule

input: list[list[]]
output: True/False

difficult
how to define the sub_box number -> utilize the indexs [r][c]
g = r // 3 * 3 + c // 3

check many times -> set()
9 row/col/grid -> list index
row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
grid = [set() for _ in range(9)]

time: O(n * m), space: O(n * m)
n = len(board), m = len(board[0])
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not len(board) or not len(board[0]):
            return False
        
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in row[r]:
                    return False
                
                if board[r][c] in col[c]:
                    return False
                
                g = (r // 3) * 3 + c // 3
                if board[r][c] in grids[g]:
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                grids[g].add(board[r][c])
        
        return True











数独的定义:
一般由9个3×3个的九宫格組成
每一列的数字均须包含 1～9，不能缺少，也不能重复
每一行的数字均须包含 1～9，不能缺少，也不能重复
每一宮(通常是 3*3 的九宫格)的数字均须包含 1～9，不能缺少，也不能重复

思路:
这道题目不需要必须包含1～9,可以存在'.',但一定满足每一列、每一行、每一宫的数字不重复
方法是使用hash+list的数据结构,将整个board按行、按列、按宫的存储;这样每次在判断的时候只用O(1)的时间


code:
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        '''print row的结果如下:
        [set([u'3', u'5', u'7']), 
        set([u'1', u'9', u'5', u'6']), 
        set([u'9', u'8', u'6']), 
        set([u'8', u'3', u'6']), 
        set([u'1', u'8', u'3', u'4']), 
        set([u'2', u'7', u'6']), 
        set([u'8', u'2', u'6']), 
        set([u'1', u'9', u'5', u'4']), 
        set([u'9', u'8', u'7'])]'''
        #意思是一共9行,每一行都用set来存储该行的内容('.'不存储),这样在每次判断某一行是否存在相同数字时,只用O(1)的时间
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        grid = [set() for i in range(9)]
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                    
                if board[r][c] in row[r]:
                    return False
                
                if board[r][c] in col[c]:
                    return False
                
                #这里利用了python的除法只取整的特性,eg:1/3 = 0
                #这样计算能算出这个点应该是属于哪一宫中(数学问题,真实牛逼....)
                g = r / 3 * 3 + c / 3
                if board[r][c] in grid[g]:
                    return False
                
                grid[g].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                
        return True
        
