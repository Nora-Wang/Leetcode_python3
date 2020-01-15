题目：
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.


思路：
实现的基本思路就是每次考虑当前node改变一个letter后，若在wordlsit中且还没有visit过，则加入queue
分层bfs，记录step数；每一层为上一层node在改变一个letter后，存在于wordlsit中所有的可能性

注意：
1.step的设计
2.wordlist和neighbor都为set，因为list在for i in list时是从头遍历到尾的，会出现time limit exceeded的情况，而set则为O(1)
3.26个字母的取值：string.lowercase
4.将字符串node中的其中一个指定index的值改为letter：def change_letter(self, index, letter, node)
5.get_neighbors的时间复杂度

code：
leetcode version
class Solution(object):
    def __init__(self):
        self.visited = set()
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
!!易错点#将list变为set（时间复杂度）
        wordList = set(wordList)
        
        if endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 1
        
        #bfs
        #step初始化为1，因为beginword相当于step1（题目结果不是edge，而是node）
        #以beginword->node->endword为例:
        #beginword为step=1
        #第一次for循环结束所得到的node被放入queue，step=2；
        #然后for循环node，如果发现node.neighbor==endword，那就再加个1，即step=3
        step = 1
        queue = collections.deque([beginWord])
        self.visited.add(beginWord)
        
        while queue:
            #后续queue在不断append，因此需要提前记录该层的queue个数
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                neighbors = self.get_neighbors(node, wordList)
                for neighbor in neighbors:
                    #若直接找到endWord
                    #注意coding style
                    if neighbor == endWord:
                        step += 1
                        return step
                
                    if neighbor in self.visited:
                        continue
                    self.visited.add(neighbor)
                    queue.append(neighbor)
            step += 1
            
        return 0
    
    #时间复杂度：O(25*L^2)
    #find the neighbors
    def get_neighbors(self, node, wordList):
        neighbors = set()
        for index in range(len(node)): #O(L)
            #方法一
            for letter in string.lowercase: #O(25)
                new_node = self.change_letter(index, letter, node) #O(L)
                if (new_node in wordList) and (new_node not in self.visited): #O(L) not O(1)
                    neighbors.add(new_node)
                    
            #方法二(快很多)
            left, right = word[:i], word[i+1:]
            for letter in string.lowercase:
                if letter == word[i]:
                    continue
                new_word = left + letter + right
                if new_word in wordList and new_word not in self.visited:
                    neighbors.add(new_word)
                    
        return neighbors
    
    #change a letter in node
    def change_letter(self, index, letter, node):
        list_node = list(node)
        list_node[index] = letter
        return ''.join(list_node)
                    
            
                    
更新版本:
class Solution(object):
    def __init__(self):
        self.visited = set()
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
 ###要记得把wordList变为set,否则会超时
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        if beginWord == endWord:
            return 1
        
        queue = collections.deque([beginWord])
        level = 1
        self.visited.add(beginWord)
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                neighbors = self.get_neighbors(word, wordList)
                for neighbor in neighbors:
                    if neighbor == endWord:
                        return level
                    
                    queue.append(neighbor)
                    
        return 0
            
    def get_neighbors(self, word, wordList):
        neighbors = set()
        
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for letter in string.lowercase:
                new_word = left + letter + right
                
                if new_word in wordList and new_word not in self.visited:
                    self.visited.add(new_word)
                    neighbors.add(new_word)
                    
        return neighbors
        
        
        

 
################follow up#############
1.要求把最短路径输出：可直接在bfs中进行更改
2.要求把所有最短路径输出：用dfs(word ladder II)
######################################

#follow up 1更改：
#到达key(node)的最短路径从哪来（pre node = {}）,存任意一个
        
class Solution(object):
    def __init__(self):
        self.visited = set()
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        if beginWord == endWord:
            return 1
        
        queue = collections.deque([beginWord])
        level = 1
        self.visited.add(beginWord)
        prev = {}
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                neighbors = self.get_neighbors(word, wordList)
                for neighbor in neighbors:
                    if neighbor == endWord:
                        prev[endWord] = word
                        self.print_path(prev, endWord, beginWord)
                        
                    prev[neighbor] = word
                    queue.append(neighbor)
                    
        return 0
    
    def print_path(self, prev, endWord, beginWord):
        path = []
        word = endWord
        
        while word in prev:
            path.append(word)
            #一定要记得renew一下word
            word = prev[word]
        
        #记得把beginword加进去
        path.append(beginWord)
        #记得倒一下
        path.reverse()
        
        print ' -> '.join(path)
    
    def get_neighbors(self, word, wordList):
        neighbors = set()
        
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for letter in string.lowercase:
                new_word = left + letter + right
                
                if new_word in wordList and new_word not in self.visited:
                    self.visited.add(new_word)
                    neighbors.add(new_word)
                    
        return neighbors
        
        
