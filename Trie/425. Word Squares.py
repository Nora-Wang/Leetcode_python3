Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:

There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).



剪枝:
1.第一个词填了ball后,第二个词必须以a开头;第二个词填了area后,第3个词必须以le开头;而以其他开头的就没必要搜下去了
第一个单词的第二个字母是第二个单词的起始字母,
第一个单词和第二个单词的第三个字母是第三个单词的前两个字母,
前三个单词的第四个字母, 是第四个单词的 前三个字母.

实现:在每个node处记录以当前node path为前缀(prefix)有哪些单词(word_list);例如以l开头的有lead,lady,以le开头的有lead,以lea开头的有lead;
这样每次只用从特定开头的单词中继续往后搜即可

2.第一个词填了ball,第二个词如果想填area,则word_list中必须要有以le/la开头的单词,否则第二个词不能填area


code:
class TrieNode(object):
    def __init__(self):
        self.children = {}
        #这道题其实is_word用不上,但为了Trie的完整性,还是加上了
        self.is_word = False
        #这道题的重点就是利用word_list来记录当前node path所形成的prefix具有哪些word
        self.word_list = []

#常规的创建Trie(除了find和startwith的返回值不同)
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            #将word记录在node path的每个node word_list中
            node.word_list.append(word)
            node = node.children[char]
        
        node.is_word = True
    
    def find(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            
        #这里需要返回node,这样便于startwith得到word_list
        return node
    
    def startwith(self, prefix):
        node = self.find(prefix)

        if node:
            return node.word_list
        return []

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        #初始化trie
        trie = Trie()
        for word in words:
            trie.add(word)
        
        #squares是最后的所有结果,而square则是每次以不同单词开头并成功的一种结果;应题目,squares为list
        squares = []
        for word in words:
            self.search(trie, [word], squares)
        
        return squares
    
    #递归的定义:利用trie,以不同word开头看能不能得到一个符合要求的square,若可以,则加入squares
    def search(self, trie, square, squares):
        # eg. ['wall', 'area'] n: 单词长度 4, pos: 单词数目 2
        n, pos = len(square[0]), len(square)
        
        # 递归出口 - 需要deep copy
        if n == pos:
            squares.append(list(square))
            return
        
        # 剪枝 - 以后面为前缀的是否存在
        #eg: 因为当前square为['wall', 'area'],则第三/四个单词一定是以le/la开头的,判断trie中是否存在以le/la开头的单词;
        #若不存在则说明第二个单词不能是area
        for col in range(pos, n):
            prefix = ''.join(square[i][col] for i in range(pos))
            if not trie.startwith(prefix):
                return
        
        # ['wall',
        #  'area']  prefix = 'le'，下一个应该以le开头，每行的pos - 2
        prefix = ''.join(square[i][pos] for i in range(pos))
        #得到以le开头的word_list
        word_list = trie.startwith(prefix)
        
        # 递归拆解 - 将word_list中的每个word都分别加入square,然后看是否满足
        #eg:对于以le开头的word_list来说,recursion每个word,进入下一层寻找
        for word in word_list:
            square.append(word)
            self.search(trie, square, squares)
            square.pop()
            
