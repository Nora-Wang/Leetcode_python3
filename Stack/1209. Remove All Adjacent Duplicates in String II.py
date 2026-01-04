Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.


# 01/04/2026
# Solution 1: Stack
# Time O(n), Space O(n)
 class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        record = []

        for char in s:
            if not len(record) or char != record[-1][0]:
                record.append([char, 1])
                continue
            
            record[-1][1] += 1
            
            if record[-1][1] == k:
                record.pop()

        return ''.join(char * count for char, count in record)
            


# Solution 2: Two Pointer
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        i, count = 0, [0] * n

        for j in range(n):
            s[i] = s[j]

            if i > 0 and s[i] == s[i - 1]:
                count[i] = count[i - 1] + 1
            else:
                count[i] = 1
            
            if count[i] == k:
                i -= k
            
            i += 1
        
        return ''.join(s[:i])
 

#brute force
#time: O(k*n), space: O(n)
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:
            return ''
        
        res = []
        for c in s:
            res.append(c)
            #这一步相当于for循环res[-k:]，判断每个数是不是都是res[-1]
            if len(res) >= k and res[-k:] == [res[-1]] * k:
                for _ in range(k):
                    res.pop()
        
        return ''.join(res)
        
        
        
#optimize
#record the chars from s into a stack. if curt char == stack[-1][-1] -> varify length of stack[-1] ?= k - 1 -> if yes, pop stack[-1]; else, to the next char
#if curt char != stack[-1][-1] -> stack append [char]
#time: O(n), space: O(n)
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:
            return ''
        
        record = []
        for c in s:
            if not record or c != record[-1][-1]:
                record.append([c])
            else:
                if len(record[-1]) == k - 1:
                    record.pop()
                else:
                    record[-1].append(c)
        
        #curt record is list[list] -> cannot use join function directly -> turn all elements into one list
        res = []
        for char in record:
            #use extend to save space
            res.extend(char)
        
        return ''.join(res)
        
                
        
