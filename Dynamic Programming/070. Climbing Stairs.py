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



#recursion -> TLE
class Solution:
    def climbStairs(self, n: int) -> int:
        return n if n <= 2 else self.climbStairs(n - 1) + self.climbStairs(n - 2)
    
#dynamic programming 
#dp[i] means all of the possibilities for curt stair i
#dp[i] = dp[i - 1] + dp[i - 2] means choose step 1 from dp[i - 1] or choose step 2 from dp[i - 2]
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
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        one = 1
        two = 1
        
        for i in range(2, n + 1):
            curt = one + two
            two = one
            one = curt
        
        return curt

    
