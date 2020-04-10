Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.



code:
#use a stack
#time O(n), space O(n)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_ = self.renew(S)
        t_ = self.renew(T)
        
        return s_ == t_
    
    def renew(self, s):
        res = []
        
        for i in range(len(s)):
            if s[i] == '#':
                if res:
                    res.pop()
            else:
                res.append(s[i])
        
        return res
        
        
        
Follow up:

Can you solve it in O(N) time and O(1) space?
#Two pointer
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = len(S) - 1
        t = len(T) - 1
        s_skip = 0
        t_skip = 0
        
        while True:
            while s >= 0 and (S[s] == '#' or s_skip):
                s_skip += 1 if S[s] == '#' else -1
                s -= 1
            
            while t >= 0 and (T[t] == '#' or t_skip):
                t_skip += 1 if T[t] == '#' else -1
                t -= 1
            
            if not (s >= 0 and t >= 0 and S[s] == T[t]):
                return s == t == -1
            
            s -= 1
            t -= 1
            
