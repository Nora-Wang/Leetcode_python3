Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.


Trie的定义


code:
#一定要另外定义Trie的data structure,因为后续每次调用函数的时候都需要直接从整棵树的root开始
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        #每次插入数据时,要从root开始,到char不同时才分叉
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        #is_word用于记录从root到该node的整个path能构成一个word,这样便于后续的search function
        node.is_word = True
         

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        #每次查找数据时,也要从root开始,到char不同时才分叉
        node = self.root
        
        for char in word:
            #不在时直接返回False
            if char not in node.children:
                return False
            node = node.children[char]
        
        #结果不一定是word,也可能是word的中间部分,因此需要用is_word判断;eg: word = inter, search = inte, return False
        return node.is_word
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        #只要有结果,就直接返回True
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
