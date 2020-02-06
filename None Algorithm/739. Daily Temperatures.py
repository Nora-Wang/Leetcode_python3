Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].


单调栈
注意stack[-1]代表的是栈最右边的值

#第1次for循环,不进入while
#print(i, T[i])
0 73
#第2次for循环,进入while,74与栈顶73比较,pop 73
#print(i, T[i], stack[-1], T[stack[-1]], i - stack[-1])
1 74 0 73 1
1 74
#第3次for循环,进入while,75与栈顶74比较,pop 74
2 75 1 74 1
2 75
#第4次for循环
3 71
#第5次for循环
4 69
#第6次for循环,进入while,72与栈顶69比较,pop 69
5 72 4 69 1
#继续while,72与栈顶71比较,pop 71
5 72 3 71 2
5 72
#第7次for循环,进入while,76与栈顶72比较,pop 72
6 76 5 72 1
#继续while,76与栈顶75比较,pop 75
6 76 2 75 4
6 76
#第8次for循环
7 73




code:
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        
        result = [0] * len(T)
        stack = []
        
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return result
