Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.



从end到start做一次BFS,并且把距离end的距离都保存在distance中
然后在从start到end做一次DFS,每走一步必须确保离end的distance越来越近




code:

leetcode Version:

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        
        if endWord not in wordList:
            return []
        
        wordList.add(beginWord)
        
        distance = {}

        self.bfs(endWord, wordList, distance)
        
        results = []
        self.dfs(distance, beginWord, results, endWord, [beginWord])
        
        return results
    
    def bfs(self, endWord, wordList, distance):
        queue = collections.deque(set([endWord]))
        distance[endWord] = 0
        
        while queue:
            word = queue.popleft()
            neighbors = self.get_neighbors(word, wordList)
            for neighbor in neighbors:
                if neighbor not in distance:
                    distance[neighbor] = distance[word] + 1
                    queue.append(neighbor)
    
    def get_neighbors(self, word, wordList):
        neighbors = set()
        #一个单词最多有len(word)个字符
        for index in range(len(word)):
            left, right = word[:index], word[index + 1:]
            #每个字符有25种不同的变化(26个字母除掉这个位置上的字母)
            for letter in string.lowercase:
                if letter == word[index]:
                    continue
                #然后check一下在不在dict里就知道是不是neighbors了
                new_word = left + letter + right
                if new_word in wordList:
                    neighbors.add(new_word)
                    
        return neighbors
            
        
    def dfs(self, distance, curt, results, endWord, path):
        if curt == endWord:
            results.append(list(path))
            return

        neighbors = self.get_neighbors(curt, distance)
        print neighbors
        for neighbor in neighbors:
            if distance[neighbor] != distance[curt] - 1:
                continue
            path.append(neighbor)
            self.dfs(distance, neighbor, results, endWord, path)
            path.pop()
        
        
        
        
lintcode Version:

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        
        distance = {}
        self.bfs(end, dict, distance)
        
        print distance
        
        results = []
        self.dfs(distance, start, end, [start], results)
        
        return results
        
    def bfs(self, end, dict, distance):
        queue = collections.deque([end])
        distance[end] = 0
        
        while queue:
            word = queue.popleft()
            neighbors = self.get_neighbors(word, dict)
            for neighbor in neighbors:
                if neighbor in distance:
                    continue
                distance[neighbor] = distance[word] + 1
                queue.append(neighbor)
                    
    def get_neighbors(self, word, dict):
        neighbors = set()
        for index in range(len(word)):
            left, right = word[:index], word[index + 1:]
            
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                if letter == word[index]:
                    continue
                new_word = left + letter + right
                if new_word in dict:
                    neighbors.add(new_word)
                    
        return neighbors
        
        
    def dfs(self, distance, curt, end, path, results):
        if curt == end:
            results.append(list(path))
            return
        
        neighbors = self.get_neighbors(curt, distance)
        print neighbors
        for neighbor in neighbors:
            if distance[neighbor] != distance[curt] - 1:
                continue
            path.append(neighbor)
            self.dfs(distance, neighbor, end, path, results)
            path.pop()
            
