Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:

Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:

You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.


code:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.add(word)
    
    def add(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        node = self.root
        
        for i in range(len(word)):
            new_word = word[:i] + '.' + word[i+1:]
            #注意这题一模一样的是false,因此带入原始word+index,这样在后续for循环的时候若c与原来的字母一样,则跳过
            if self.helper(new_word, node, word, i):
                return True
        
        return False
    
    def helper(self, word, node, o_word, index):
        if not word:
            return node.is_word
        
        char = word[0]
        
        if char == '.':
            for c in node.children:
                if o_word[index] == c:
                    continue
                if self.helper(word[1:], node.children[c], o_word, index):
                    return True
            return False
        
        else:
            if char not in node.children:
                return False
            return self.helper(word[1:], node.children[char], o_word, index)
    


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
