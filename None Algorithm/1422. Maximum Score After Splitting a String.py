Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3
Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
Example 3:

Input: s = "1111"
Output: 3
 

Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.

# time: O(n), space: O(1)
class Solution:
    def maxScore(self, s: str) -> int:
        count_1 = s.count('1')
        count_0 = 0
        max_score = 0
        
        # 这里的范围要注意：edge case '00', 若为len(s),则结果为2('00' + ''),但题目要求right一定有值
        for i in range(len(s) - 1):
            if s[i] == '0':
                count_0 += 1
            else:
                count_1 -= 1
            
            max_score = max(max_score, count_0 + count_1)
        
        return max_score




# time: O(n), space: O(n)
class Solution:
    def maxScore(self, s: str) -> int:
        count_0 = [0] * (len(s) + 1)
        count_1 = [1] * (len(s) + 1)
        
        for i,c in enumerate(s):
            if c == '0':
                count_0[i + 1] = count_0[i] + 1
                count_1[i + 1] = count_1[i]
            else:
                count_1[i + 1] = count_1[i] + 1
                count_0[i + 1] = count_0[i]
        
        max_score = float('-inf')
        for i in range(1, len(s)):
            max_score = max(max_score, count_0[i] + count_1[-1] - count_1[i])
        
        return max_score
