You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.


# Solution 1: Array
class Solution:
    def removeDuplicates(self, s: str) -> str:
        record = []

        for char in s:
            if not len(record) or record[-1] != char:
                record.append(char)
                continue
            
            while len(record) and char == record[-1]:
                record.pop()
        
        return ''.join(record)
            

# Simplify Version
class Solution:
    def removeDuplicates(self, s: str) -> str:
        record = []

        for char in s:
            if len(record) and char == record[-1]:
                record.pop()
            else:
                record.append(char)
        
        return ''.join(record)
            

# Solution 2: Two Pointer
class Solution:
    def removeDuplicates(self, s: str) -> str:
        list_s = list(s)
        i = 0

        for j in range(len(list_s)):
            list_s[i] = list_s[j]

            if i > 0 and list_s[i] == list_s[i - 1]:
                i -= 2
            
            i += 1
        
        return ''.join(list_s[:i])
