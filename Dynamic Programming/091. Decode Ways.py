A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

  
# 1/19/21
# time: O(n), space: O(n)
'''
s = '2' -> 1
s = '22' -> 2
s = '226' -> '2' + '26' or '22' + '6' -> 3
              dp['2']       dp['22']
              
dp[i] += dp[i - 2] + dp[i - 1] if match the rules              
'''              
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        dp = [0] * len(s)
        dp[0] = 1 if s[0] != '0' else 0
        
        for i in range(1, len(s)):
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i - 2] if i >= 2 else 1
            if s[i] != '0':
                dp[i] += dp[i - 1]
                
        return dp[-1]
  
# space optimal
# time: O(n), space: O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        prev_prev = 1
        prev = 1 if s[0] != '0' else 0
        
        for i in range(1, len(s)):
            curt = 0
            if 10 <= int(s[i-1:i+1]) <= 26:
                curt += prev_prev
            if s[i] != '0':
                curt += prev
                
            prev_prev = prev
            prev = curt
                
        return prev
  
  
  
  
  
  
# DP
# time: O(n), space: O(n)
'''
s = '2' -> 1
s = '22' -> 2
s = '226' -> '2' + '26' or '22' + '6' -> 3
              dp['2']       dp['22']

dp[i]: how many decode methods for s[:i] 0 ~ i - 1
if dp[i - 2] exist and 10 <= int(s[i - 2:i]) <= 26 -> dp[i] += dp[i - 2]
if 1 <= int(s[i - 1]) <= 9 -> dp[i] += dp[i - 1]

'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            if dp[i - 2] and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
            
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]
        
        return dp[-1]
    
    
# DFS (TLE)
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        self.res = 0
        self.helper(s, 0, '')
        
        return self.res
    
    def helper(self, s, index, last):
        if index == len(s):
            self.res += 1
            return 
        
        # single
        if s[index] != '0':
            self.helper(s, index + 1, s[index])
        
        # two
        if last and 10 <= int(last + s[index]) <= 26:
            self.helper(s, index + 1, '')
    
    
    
    

思路：
参考DP经典题目上楼梯问题：n节楼梯从第0层开始，每次只能1层或2层，问上到第n层有 多少种方法?
解决方案：f[n]表示从第0层走到第n层一共有多少种方法，f[n] = f[n-1] + f[n-2]，时间复杂度为O(n)
注意：一般f[0]都为1


此题思路同上楼梯问题：
result[n] = result[n-1] + result[n-2]
有result[n-2]的条件是result[n-2]存在,并且s[n-1]与s[n]组成的数字在10-26之间
有result[n-1]的条件result[n-1]存在,并且s[n - 1]!=0

eg:
s = “12”
n.     0 1 2
s        1 2
result 1 1 2
1.n = 1时,因为不存在result[n - 2],因此不用加result[n - 2],并且由于存在result[n - 1] and s[0]不为0 -> result[1] = result[0] = 1
2.n = 2时,因为存在result[n - 2] and 12在10~26范围内,并且由于存在result[n - 1] and s[1]不为0 -> result[2] = result[0] + result[1] = 2


code:
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        result = [0] * (len(s) + 1)
        result[0] = 1
        
        for i in range(1, len(result)):
            #注意s取的方式
            #由于s的index会空一个,因此其取值应该是result的index - 1(逻辑问题)
            #s为string,需要提前int才能与数字比较大小
            if result[i - 2] and 10 <= int(s[i - 2 : i]) <= 26:
                result[i] += result[i - 2]
            
            if result[i - 1] and s[i - 1] != '0':
                result[i] += result[i - 1]
                
        return result[-1]
