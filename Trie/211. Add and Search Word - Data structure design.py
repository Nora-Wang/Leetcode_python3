Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.


Trie的定义 + DFS recursion

code:
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_word = True

    #当char = '.'时,需要将所有sub_node都遍历一次,若存在word则返回True;因此用recursion的方法来做
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(word, 0, self.root)
    
    
    def find(self, word, index, node):
        #递归出口
        if index == len(word):
            #因为是search word,不是startwith,因此需要返回是否为word
            return node.is_word
        
        #获取当前字母
        char = word[index]
        #如果不是'.'，正常判断是否在node.children，递归到下一层
        if char != '.':
            if char not in node.children:
                return False
            
            return self.find(word, index + 1, node.children[char])
           
        #如果是'.'，遍历node.children里的每一个点，一旦找到符合的，就返回True 
        for sub_node in node.children:
            if self.find(word, index + 1, node.children[sub_node]):
                return True
        
        return False
            
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
