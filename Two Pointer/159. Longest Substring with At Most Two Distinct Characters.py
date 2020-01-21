Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.


基本是同向双指针模板问题

code:
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = {}
        j = 0
        max_length = 0
        
        for i in range(len(s)):
            #这里的判定条件需要考虑清楚:record中的letter个数小于2或者s[j]在record里时,都是满足条件的
            while j < len(s) and (len(record) < 2 or s[j] in record):
                record[s[j]] = record.get(s[j], 0) + 1
                j += 1
            
            #这里也满足corner case:'a',结果为1
            max_length = max(max_length, j - i)
            
            record[s[i]] -= 1
            if record[s[i]] == 0:
                del record[s[i]]
            
        return max_length

                
        
