Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].


单调栈

code:
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        
        result = [0] * len(T)
        stack = []
        
        #当stack = [2,3,4]即stack代表的值为[75,71,69,72];此时T[i] = 76, stack[-1] = 2即75
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return result
