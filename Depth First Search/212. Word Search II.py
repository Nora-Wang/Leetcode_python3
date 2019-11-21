Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]



code:
DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not len(board) or not len(board[0]) or not len(words):
            return []
        
        #results可能出现重复的情况 eg: board = ["a","a"],words = ['a'],若不用set,输出结果应该为["a","a"],因为words能在board里找到两次
        results = set()
        
        #检查path在不在words里用set时O(1)
        words = set(words)
        
        #建立prefix_set来存前缀 
        #例如["eat","oath"]就存为 set([e, ea, eat, o, oa, oat, oath]) 
        #注意写法
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(board, words, prefix_set, row, col, board[row][col], set([(row, col)]), results)
        
        #结果为[],需要转换一下
        return list(results)
    
    def dfs(self, board, words, prefix_set, row, col, temp, visited, results):
        #递归出口
        #如果当前temp就是words,加入结果
        if temp in words:
            results.add(temp)
        
        #递归解析
        #向四周寻找
        for dir_r, dir_c in DIRECTIONS:
            new_row, new_col = row + dir_r, col + dir_c
            
            #不符合条件的情况
            #1.range
            if not (0 <= new_row < len(board) and 0 <= new_col < len(board[0])):
                continue
            #已经被走过
            if (new_row, new_col) in visited:
                continue
            #如果当前temp + board[new_row][new_col]不在prefix_set中
            if (temp + board[new_row][new_col]) not in prefix_set:
                continue

            visited.add((new_row, new_col))
            self.dfs(board, words, prefix_set, new_row, new_col, temp + board[new_row][new_col], visited, results)
            visited.remove((new_row, new_col))
        
                
