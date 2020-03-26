In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
 

Note:

The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000


code:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_word = True
    
    def search(self, word):
        node = self.root
        
        #这里for循环的处理很关键
        for i in range(len(word)):
            #只要当前是word,就输出
            #满足条件: If a successor has many roots can form it, replace it with the root with the shortest length.
            if node.is_word:
                return word[:i]
            
            #trie走到头
            if not node.children:
                break
            
            #当前char不在children里,即不在trie里
            if word[i] not in node.children:
                break
            
            node = node.children[word[i]]
        
        return word
        
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dict:
            trie.add(word)
        
        sentence = sentence.split()
        
        for i in range(len(sentence)):
            new_word = trie.search(sentence[i])
            
            sentence[i] = new_word
        
        return ' '.join(sentence)
