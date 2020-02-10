A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.


code:
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        hash_table_end = {}
        
        #记录每个字母最后一次出现的index
        for i in range(len(S) - 1, -1, -1):
            if S[i] in hash_table_end:
                continue
            hash_table_end[S[i]] = i
        
        index = 0
        result = []
        while index < len(S):
            #start记录第一个字母第一次出现的index
            start = index
            #right记录第一个字母最后一次出现的index
            right = hash_table_end[S[index]]
            
            #直到index走到right时,right一直取所有字母的max值
            while index != right:
                index += 1
                right = max(right, hash_table_end[S[index]])
            
            #这里记得+1,start = 0, end = 8,之间存在9个数
            result.append(right - start + 1)
            
            index += 1
        
        return result
            
            
        
        
        
        
        
