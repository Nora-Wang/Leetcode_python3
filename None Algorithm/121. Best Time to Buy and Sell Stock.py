Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

code:
1. 一个是扫三遍，得到每个位置的左边数最小值和右边数最大值，求最大差
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = []
        curt_min, curt_max = sys.maxsize, -sys.maxsize
        for num in prices:
            curt_min = min(curt_min, num)
            left.append(curt_min)
        
        right = []
        for i in range(len(prices) - 1, -1, -1):
            curt_max = max(curt_max, prices[i])
            right.append(curt_max)
        right.reverse()
        
        res = 0
        for i in range(len(left)):
            res = max(res, right[i] - left[i])
        
        return res
        
        
2. 生成一个单调栈，每次用栈的最后一个数减第一个数
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        stack = []
        res = 0
        for i in range(len(prices)):
            while stack and prices[i] <= stack[-1]:
                stack.pop()
            
            stack.append(prices[i])
            res = max(res, stack[-1] - stack[0])
        
        return res
            
            
            
            
3. 找一个当前最小值，每一位减去当前最小值，求最大的差
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        curt_min = prices[0]
        distance = 0
        result = 0
        index = 0
        for i in range(1, len(prices)):
            if prices[i] < curt_min:
                curt_min = prices[i]
                distance = 0
                continue
                
            if prices[i] - curt_min > distance:
                index = i
                distance = prices[i] - curt_min
                result = max(result, distance)

        return result
