You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:

Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:

The number of given pairs will be in the range [1, 1000].


差不多是DP模板

code:
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not len(pairs) or not len(pairs[0]):
            return 0
        
        #需要提前排个序
        #注意lists中list的第一个数为标准排序写法
        pairs.sort(key = lambda x : x[0])
        
        dp = [1] * len(pairs)
        
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        
        return max(dp)
