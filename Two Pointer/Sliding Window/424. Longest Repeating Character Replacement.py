Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


'''
while right < len(s):
    window: s[left:right]
    record = {char:freq}
    max_freq: the maximum freq of the char in curt window
    diff: the rest different char in curt window (need to be change) = right - left - max_freq
    
    while right < len(s) and diff <= k -> move right pointer
    else: 1. right == len(s) and diff <= k -> right - left
          2. right == len(s) and diff == k + 1 -> right - left - 1
          3. right < len(s) and diff == k + 1 -> right - left - 1

time: O(n), space: O(n)

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        left, right = 0, 0
        record = collections.defaultdict(int)
        max_freq = 0
        res = 0
        
        while right < len(s):
            while right < len(s) and right - left - max_freq <= k:
                record[s[right]] += 1
                max_freq = max(max_freq, record[s[right]])
                right += 1
            
            if right - left - max_freq == k + 1:
                res = max(res, right - left - 1)
            elif right == len(s):
                res = max(res, right - left)
            
            record[s[left]] -= 1
            left += 1
        
        return res
            
            
            
