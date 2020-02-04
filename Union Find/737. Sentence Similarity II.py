Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].



code:
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        
        self.father = {}
        
        #self.father的初始化,将pairs中的数据进行union
        for x,y in pairs:
            if x not in self.father:
                self.father[x] = x
            if y not in self.father:
                self.father[y] = y
            
            self.union(x,y)
        
        #判断words1和words2是否匹配
        for i in range(len(words1)):
            #若不在self.father中,则初始化一下,不能直接return False
            #eg: words1 = ["I","have","enjoyed","happy","thanksgiving","holidays"]
            #    words2 = ["I","have","enjoyed","happy","thanksgiving","holidays"]
            #但是pairs中并没有这些words的数据,此时直接比较两者即可
            if words1[i] not in self.father:
                self.father[words1[i]] = words1[i]
            if words2[i] not in self.father:
                self.father[words2[i]] = words2[i]
            
            if self.find(words1[i]) != self.find(words2[i]):
                return False
        
        return True
    
    def union(self, point_a, point_b):
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        
        if root_a != root_b:
            self.father[root_a] = root_b
    
    def find(self, point):
        path = []
        
        while self.father[point] != point:
            path.append(point)
            point = self.father[point]
        
        for p in path:
            self.father[p] = point
        
        return point
