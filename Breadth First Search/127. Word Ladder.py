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




code：
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
        if endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 1
        
        step_level = 1
        queue = collections.deque(beginWord)
        while queue:
            step_level += 1
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                neighbors = self.get_neighbors(node, wordList)
                for neighbor in neighbors:
                    if neighbor == endWord:
                        return step_level
                    queue.append(neighbor)
                    self.visited.add(neighbor)
        return 0
    
    def get_neighbors(self, node, wordList):
        neighbors = []
        for index in range(len(node)):
            for letter in range(97,110):
                letter_replaced_node = self.replace_letter(index, chr(letter), node)
                if letter_replaced_node in wordList:
                    if letter_replaced_node not in self.visited:
                        neighbors.append(letter_replaced_node)
        return neighbors
    
    
    def replace_letter(self, index, letter, node):
        list_node = list(node)
        list_node[index] = letter
        return ''.join(list_node)
                    
            
