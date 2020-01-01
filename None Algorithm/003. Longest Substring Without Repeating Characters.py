Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             

思路:
Hash + sliding window 一边增加 一边减少(双指针)
先找到s[0]开头的最长的string,然后就是sliding window,在hash表中将减去头部的s[i],然后再进行向后延伸
             
code:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique = set()
        longest = 0
        n = len(s)
        j = 0
        
        for i in range(n):
            #注意这里的意思是将头部的s[i]删除,然后看从s[i + 1]开始的最长string;其中间部分s[i+1:j-1]都是一样的,因此直接从j开始寻找即可
            while j < n and s[j] not in unique:
                unique.add(s[j])
                j += 1
            
            longest = max(longest, j - i)
            unique.remove(s[i])
            
        return longest
        
        
