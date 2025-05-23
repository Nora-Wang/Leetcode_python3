Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.

# Backtracking
# Time O(2^n * n), Space O(n)
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.res = 1
        
        self.helper(s, 0, set())
        
        return self.res
    
    def helper(self, s, left, visited):
        if left == len(s):
            self.res = max(self.res, len(visited))
            return
        
        for right in range(left + 1, len(s) + 1):
            char = s[left:right]
            
            if char not in visited:
                visited.add(char)
                self.helper(s, right, visited)
                visited.remove(char)
        
        return


# Backtracking + Pruning
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.res = 1
        
        self.helper(s, 0, set())
        
        return self.res
    
    def helper(self, s, left, visited):
        if left == len(s):
            self.res = max(self.res, len(visited))
            return

        # Pruning: if current unique chars + the lenght of rest string chara <= self.res
        if len(visited) + len(s) - left <= self.res:
            return
        
        for right in range(left + 1, len(s) + 1):
            char = s[left:right]
            
            if char not in visited:
                visited.add(char)
                self.helper(s, right, visited)
                visited.remove(char)
        
        return
