Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true



# time: O(n), space: O(1) (max space is 128, only 128 char in string)
# Hashtable
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = collections.Counter(s)
        
        single = 0
        for _,num in count.items():
            if num % 2:
                single += 1
        
        return single <= 1
        
        
# Array
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        map = [0] * 128
        count = 0
        for c in s:
            map[ord(c)] += 1
            if map[ord(c)] % 2:
                count += 1
            else:
                count -= 1
        
        return count <= 1
