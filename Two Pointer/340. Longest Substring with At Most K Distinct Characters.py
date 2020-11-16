Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.


'''
window + hashtable

while right < len(s):
    1. create avaliable window[left:right] -> at most has k distinct chars or curt char is the same as previous char in window
        hash_s = {char:freq}
    2. renew res
    3. move window -> move left, renew distinct and hash_s

time: O(n), space: O(n)
'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k < 1:
            return 0
        
        hash_s = collections.defaultdict(int)
        res = 0
        left, right = 0, 0
        
        while right < len(s):
            # create window
            while right < len(s) and (len(hash_s) < k or s[right] in hash_s):
                hash_s[s[right]] += 1
                right += 1
            
            # renew res
            res = max(res, right - left)
            
            # move window
            hash_s[s[left]] -= 1
            if hash_s[s[left]] == 0:
                del hash_s[s[left]]
            left += 1
        
        return res
            
            
    
    
    
    
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
