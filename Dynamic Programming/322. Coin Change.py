You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4


# Version 1: DFS
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        
        coins.sort(reverse=True)
        self.res = float('inf')
        
        self.helper(coins, 0, 0, amount)
        
        return self.res if self.res != float('inf') else -1
    
    def helper(self, coins, index, count, amount):
        # 这个要写在index == len(coins)前面，因为可能当index == len(coins)时，当前amount刚好为0，若index == len(coins)写在前面则这种情况将不被算在内
        # eg: [1,2,5], 11 -> 5 + 5 + 1, 最后一层recursion时, index = len(coins), count = 3，amount = 1
        if amount == 0:
            self.res = min(self.res, count)
            return
        
        if index == len(coins):
            return
        
        # prune
        # 1. amount exceeded (pass 32)
        # 2. curt coins count is larger that curt_min_count/self.res (pass 62)
        # 3. rest coins are not enough for rest amount (pass 179/182)
        if amount < 0 or count >= self.res:
            return
        if amount // coins[index] > self.res - count:
            return
        
        for i in range(amount // coins[index], -1, -1):
            self.helper(coins, index + 1, count + i, amount - coins[index] * i)
