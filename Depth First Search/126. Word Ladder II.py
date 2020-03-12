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



从end到start做一次BFS,并且把距离end的长度都保存在distance中
然后在从start到end做一次DFS,每走一步必须确保离end的distance越来越近



#3/12/2020
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        
        if endWord not in wordList:
            return []
        
        wordList.add(beginWord)
        
        distances = self.bfs(endWord, wordList)
        
        res = []
        self.dfs(beginWord, endWord, wordList, [beginWord], res, distances)
        
        return res
    
    def bfs(self, endWord, wordList):
        distances = {}
        
        distances[endWord] = 0
        queue = collections.deque([endWord])
        
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                
                neighbors = self.get_neighbors(word, wordList)
                
                for neighbor in neighbors:
                    if neighbor not in distances:
                        distances[neighbor] = distances[word] + 1
                        queue.append(neighbor)
        
        return distances
    
    def dfs(self, curt, endWord, wordList, temp, res, distances):
        if curt == endWord:
            res.append(list(temp))
            return
        
        neighbors = self.get_neighbors(curt, wordList)
        
        for neighbor in neighbors:
            if distances[neighbor] != distances[curt] - 1:
                continue
                
            temp.append(neighbor)
            self.dfs(neighbor, endWord, wordList, temp, res, distances)
            temp.pop()
    
    def get_neighbors(self, word, wordList):
        neighbors = []
        
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            
            for c in string.ascii_lowercase:
                if c == word[i]:
                    continue
                
                new_word = left + c + right
                
                if new_word in wordList:
                    neighbors.append(new_word)
            
        return neighbors












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
        #wordList设置为set,降低时间复杂度
        wordList = set(wordList)
        
        #leetcode存在一种corner case:wordList中没有endWord,则没有结果
        if endWord not in wordList:
            return []
        
        #beginWord可能不存在于wordList里面
        wordList.add(beginWord)
        
        #key为该点,value是距离endWord的长度
        distance = {}
        
        #构建distance hash表,以为后续dfs提供数据
        self.bfs(endWord, wordList, distance)
        
        results = []
        self.dfs(distance, beginWord, results, endWord, [beginWord])
        
        return results
    
    #bfs需要从endWord开始,因为后续每找到一个符合条件的word的neighbor,其distance可直接在distance[word]基础上+1,即为该点距离endWord的长度
    #bfs记录每个点到endWord的最短距离长度
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
            
