You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


#dfs -> TLE
class Solution:
    def climbStairs(self, n: int) -> int:
        self.count = 0
        
        self.dfs(n)
        
        return self.count
    
    def dfs(self, n):
        if n == 0:
            self.count += 1
            return
        if n < 0:
            return
        
        self.dfs(n - 1)
        self.dfs(n - 2)
        


#recursion -> TLE
class Solution:
    def climbStairs(self, n: int) -> int:
        return n if n <= 2 else self.climbStairs(n - 1) + self.climbStairs(n - 2)
    
#dynamic programming 
#dp[i] means all of the possibilities for curt stair i
#dp[i] = dp[i - 1] + dp[i - 2] means choose step 1 from dp[i - 1] or choose step 2 from dp[i - 2], we can arrive curt stair i
#time: O(n), space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        #corner case
        if n <= 2:
            return n
        
        #initial
        dp = [0] * n
        dp[0] = 1 # n = 1 -> 1
        dp[1] = 2 # n = 2 -> 1 + 1, 2
        
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]
    
#dynamic programming
#time: O(n), space: O(1)
# V1
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        #when n = 1, only can choose step 1
        #two means after choose step 2, we can arrive curt stair
        #one means after choose step 1, we can arrive curt stair
        one = 1
        two = 1
        
        for i in range(2, n + 1):
            curt = one + two
            two = one
            one = curt
        
        return curt
#V2
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        climb1 = 1
        climb2 = 2
        
        for i in range(2, n):
            temp = climb2
            climb2 += climb1
            climb1 = temp
            
        return climb2
    
