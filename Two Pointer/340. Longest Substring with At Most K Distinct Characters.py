Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.


跟159一样,都是同向双指针问题,就是要多一个对k的判定条件

code:
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #corner case: k = 0 or k < 0
        if k < 1:
            return 0
        
        max_length = 0
        j = 0
        record = {}
        
        for i in range(len(s)):
            while j < len(s) and (len(record) < k or s[j] in record):
                record[s[j]] = record.get(s[j], 0) + 1
                j += 1
            
            max_length = max(max_length, j - i)
            
            record[s[i]] -= 1
            if record[s[i]] == 0:
                del record[s[i]]
            
        return max_length
