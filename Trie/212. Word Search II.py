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
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.


这里用Trie + DFS
还有DFS的方法,直接看DFS中的212


****************************************
result要设置为set避免重复
Input
[["a","a"]]
["a"]
Output
["a","a"]
Expected
["a"]
****************************************

code:
DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = None
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_word = True
        node.word = word
        
    def find(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node
        
class Solution(object):
    def wordSearchII(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not len(board) or not len(board[0]):
            return []
            
        #设为set,避免重复
        #eg: [['a'], ['a']], ['a']
        result = set()
        
        #初始化trie
        trie = Trie()
        for word in words:
            trie.add(word)
        
        #以board的每个char开头,判断是否能在trie中找到word
        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                self.search(board, i, j, trie.root.children.get(char), set([(i,j)]), result)
        
        #结果为list 
        return list(result)
    
    def search(self, board, x, y, node, visited, result):
        #node.children中不存在char,则说明node的剩下路都不用走了
        if not node:
            return
        
        #递归出口
        if node.is_word:
            result.add(node.word)
        
        #dfs向4个方向扩散
        for direct in DIRECTIONS:
            new_x = x + direct[0]
            new_y = y + direct[1]
            
            #判断新的点是否在board的范围内,并且不在visited里
            if self.is_valid(board, new_x, new_y, visited):
                visited.add((new_x, new_y))
                
                char = board[new_x][new_y]
                self.search(board, new_x, new_y, node.children.get(char), visited, result)
                
                #set的删除是remove
                visited.remove((new_x, new_y))
                
                
    
    def is_valid(self, board, x, y, visited):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        
        if (x,y) in visited:
            return False
            
        return True
