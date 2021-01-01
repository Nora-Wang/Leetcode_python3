Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
 

Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.





# 参考1143. Longest Common Subsequence先得到LCS，然后将剩余部分补齐即可

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        lcs = self.get_lcs(str1, str2)
        
        res = []
        i, j = 0, 0
        for c in lcs:
            # 按顺序将str1,str2中插在LCS中间的（即不是common的部分）部分按顺序先填入
            while c != str1[i]:
                res.append(str1[i])
                i += 1
            while c != str2[j]:
                res.append(str2[j])
                j += 1
                
            res.append(c)
            i += 1
            j += 1
        
        return ''.join(res) + str1[i:] + str2[j:]
    
    def get_lcs(self, str1, str2):
        res = []
        
        dp = [['' for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + str1[i]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
        
        return dp[-1][-1]
