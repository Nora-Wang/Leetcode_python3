Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.



# 12/16/2020
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i,j))
                    if self.dfs(board, word, 1, i, j, visited):
                        return True
        
        return False
    
    def dfs(self, board, word, index, x, y, visited):
        if index == len(word):
            return True
        
        for direct in [(0,1),(0,-1),(1,0),(-1,0)]:
            x_ = x + direct[0]
            y_ = y + direct[1]
            if self.is_valid(board, x_, y_, visited, word[index]):
                visited.add((x_,y_))
                if self.dfs(board, word, index + 1, x_, y_, visited):
                    return True
                visited.remove((x_,y_))
                
        return False
            
    def is_valid(self, board, x, y, visited, letter):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return False
        
        if (x,y) in visited:
            return False
        
        if board[x][y] != letter:
            return False
        
        return True
    
        
                    








****************************************
一定要注意dfs是有返回值的！！！！因此在每次调用dfs的时候都要写上返回值
****************************************


基本思路就是在给定的矩阵中dfs，去重的手法可以每次先改动matrix的当前格子，然后再改回去，目的是让dfs过程中的一条路径不会经过同样位置两次，
但不同的路径可以经过同样的位置。


code:
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]#全局变量
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not len(board) or not len(board[0]):
            return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                #当找到第一个值匹配时再进入dfs,节省时间复杂度
                if board[row][col] != word[0]:
                    continue
                    
                #因为第一个值已经是相等了,dfs可以从第一个值开始,因此visite里放入了目前的点,index也是从1开始的
                #由于dfs的返回值为True or False,只要dfs的结果为True,整个的结果就直接返回True即可
                if self.dfs(board, word, 1, row, col, set([(row, col)])):
                    return True
                
        return False
    
    #index用于记录判断到word的第几个值了,visited用于避免回去
    def dfs(self, board, word, index, row, col, visited):
        #递归出口
        #检查范围, 如果检查完了，返回True
        #这里是递归的出口，因为检查合理不合理在后面，所以这里是index == len(word) 
        #输入 [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]  "ABC#" 
        #当point指向#时候，证明ABC都符合，都已放入visited时，此时递归结束，即point == len(word) 
        if len(word) == index:
            return True
    
        for dir_r, dir_c in DIRECTIONS:
            new_row = row + dir_r
            new_col = col + dir_c
            
            #去除不符合要求的情况
            #1.超出matrix的范围
            if not (0 <= new_row < len(board) and 0 <= new_col < len(board[0])):
                continue
            #2.生成的new点之前已经visited过了
            if (new_row, new_col) in visited:
                continue
            #3.题目要求,值相等
            if board[new_row][new_col] != word[index]:
                continue
                
            #符合要求的加入visited,记录一下
            visited.add((new_row, new_col))
            if self.dfs(board, word, index + 1, new_row, new_col, visited):
                return True
            visited.remove((new_row, new_col))
        
        return False
            
        
        
        
