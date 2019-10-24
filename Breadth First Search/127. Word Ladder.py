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
        #将list变为set（时间复杂度）
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
                    if neighbor == endWord:
                        step += 1
                        return step
                    if neighbor not in self.visited:
                        self.visited.add(neighbor)
                        queue.append(neighbor)
            step += 1
        return 0
    
    #find the neighbors
    def get_neighbors(self, node, wordList):
        neighbors = set()
        for index in range(len(node)):
            for letter in string.lowercase:
                new_node = self.change_letter(index, letter, node)
                if (new_node in wordList) and (new_node not in self.visited):
                    neighbors.add(new_node)
        return neighbors
    
    #change a letter in node
    def change_letter(self, index, letter, node):
        list_node = list(node)
        list_node[index] = letter
        return ''.join(list_node)
                    
            
                    
lintcode version:
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def __init__(self):
        self.visited = set()
        
    def ladderLength(self, start, end, dict):
        if start == end:
            return 1
        dict.add(end)
        queue = collections.deque([start])
        self.visited.add(start)
        step = 1
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                neighbors = self.get_neighbors(node, dict)
                for neighbor in neighbors:
                    if neighbor == end:
                        step += 1
                        return step
                    if neighbor not in self.visited:
                        queue.append(neighbor)
                        self.visited.add(neighbor)
            step += 1
        return 0
        
    def get_neighbors(self, node, dict):
        neighbors = set()
        for index in range(len(node)):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                new_node = self.get_new_node(node, index, letter)
                if new_node in dict and new_node not in self.visited:
                    neighbors.add(new_node)
        return neighbors
    
    def get_new_node(self, node, index, letter):
        list_node = list(node)
        list_node[index] = letter
        return ''.join(list_node)
        

