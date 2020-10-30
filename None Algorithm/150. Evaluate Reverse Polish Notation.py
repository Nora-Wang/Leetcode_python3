Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


'''
clarification
1. digit: negative, positive
2. +
3. -
4. *
5. /: the division's result, round/down/up? 

edge case:
1. other situation? other invalid char?
2. divisor == 0?
3. [1, +]?
4. [1, 2, +, 1] -> [3, 1]?

find the last number in the list -> utilize stack to solve it(FILO)

time: O(n), space: O(n)
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        
        stack = []
        
        for c in tokens:
            if c.isdigit() or len(c) >= 2:
                stack.append(int(c))
                continue
            
            second = stack.pop()
            first = stack.pop()
            
            if c == '+':
                curt_sum = second + first
                stack.append(curt_sum)
            
            if c == '-':
                curt_diff = first - second
                stack.append(curt_diff)
            
            if c == '*':
                curt_pro = first * second
                stack.append(curt_pro)
            
            if c == '/':
                curt_div = first / second
                stack.append(int(curt_div))
        
        return stack[-1]
                
                
                
                
