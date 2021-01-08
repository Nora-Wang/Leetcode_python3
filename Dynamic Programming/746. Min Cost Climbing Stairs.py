On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:

Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:

Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:

cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].


'''
dp[i]: min cost from 0 to i-th step
dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
dp[0] = cost[0]
dp[1] = cost[1]
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        
        return min(dp[-1], dp[-2])
        
        
        
# space optimal
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_1 = 0
        prev_2 = 0
        
        for i in range(len(cost) - 1, -1, -1):
            temp = min(prev_1, prev_2) + cost[i]
            prev_2 = prev_1
            prev_1 = temp
        
        return min(prev_1, prev_2)
