A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

 

Example 1:

Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.
Example 2:

Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.
Example 3:

Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
 

Constraints:

1 <= expression.length <= 2 * 104
expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.


# 1. use stack to record
# 2. when meet ')', only need to use 'hasTrue, hasFalse' to record
# whether existing 't' or 'f' in this pair of closing parenthesis, then generate the result for this closing parenthesis
# Time O(n), Space O(n)


# Recursion
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        self.helper(expression, 0, stack)
        
        return stack[0] == 't'
    
    def helper(self, expression, index, stack):
        if index >= len(expression):
            return
        
        if expression[index] == '&' or expression[index] == '|' or expression[index] == '!' or expression[index] == 't' or expression[index] == 'f':
            stack.append(expression[index])
        
        if expression[index] != ')':
            return self.helper(expression, index + 1, stack)
        
        hasTrue, hasFalse = False, False
        while stack[-1] == 't' or stack[-1] == 'f':
            char = stack.pop()
            
            if char == 't':
                hasTrue = True
            if char == 'f':
                hasFalse = True
        
        op = stack.pop()
        if op == '!':
            stack.append('f' if hasTrue else 't')
        if op == '&':
            stack.append('f' if hasFalse else 't')
        if op == '|':
            stack.append('t' if hasTrue else 'f')

        # pay attention: should return and continue the index loop
        return self.helper(expression, index + 1, stack)



# Optimize: for loop
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for ex in expression:
            if ex == '(' or ex == ',':
                continue
                
            if ex != ')':
                stack.append(ex)
                continue
            
            hasTrue, hasFalse = False, False
            while stack[-1] == 't' or stack[-1] == 'f':
                char = stack.pop()
                
                if char == 't':
                    hasTrue = True
                if char == 'f':
                    hasFalse = True
            
            op = stack.pop()
            if op == '&':
                stack.append('f' if hasFalse else 't')
            if op == '!':
                stack.append('f' if hasTrue else 't')
            if op == '|':
                stack.append('t' if hasTrue else 'f')
        
        return stack[0] == 't'
            
