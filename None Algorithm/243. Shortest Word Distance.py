Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

# Version 0
'''
We can greatly improve on the brute-force approach by keeping two indices i1 and i2 where we store the most recent locations of word1 and word2. 
Each time we find a new occurrence of one of the words, we do not need to search the entire array for the other word, 
since we already have the index of its most recent occurrence.
这里的设计有点tricky，这里使得p1和p2都是最近的pair，因为只要p1和p2同时存在，则他们一定是最close的
'''
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1, p2 = -1, -1
        min_distance = len(words)
        
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
            elif words[i] == word2:
                p2 = i
                
            if p1 != -1 and p2 != -1:
                min_distance = min(min_distance, abs(p1 - p2))
        
        return min_distance


# Version 1
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        hash_index = collections.defaultdict(list)
        
        for i in range(len(words)):
            if words[i] == word1 or words[i] == word2:
                hash_index[words[i]].append(i)
        
        min_distance = len(words)
        for w1_index in hash_index[word1]:
            w2_index = self.closest_num(hash_index[word2], w1_index)
            min_distance = min(min_distance, abs(w2_index - w1_index))
        
        return min_distance
    
    def closest_num(self, w2, target):
        if len(w2) == 1:
            return w2[0]
        
        left, right = 0, len(w2) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if w2[mid] < target:
                left = mid
            else:
                right = mid
        
        return w2[left] if abs(w2[left] - target) < abs(w2[right] - target) else w2[right]





将整个数组遍历一遍


code:
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        #这些值都要初始化为最大,因为后续是取最小
        p1, p2 = sys.maxsize, sys.maxsize
        result = sys.maxsize
        
        for i in range(len(words)):
            #得到一个word1的index
            if words[i] == word1:
                p1 = i
            
            #得到一个word2的index
            if words[i] == word2:
                p2 = i
            
            #corner case:不判断的话,结果为0
            if p2 == p1 == sys.maxsize:
                continue
            
            #每一次的两两组合,求得一个最小值即可
            result = min(abs(p2 - p1), result)
        
        return result
                
