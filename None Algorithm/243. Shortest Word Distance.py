Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


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
                
