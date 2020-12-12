Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


# time: O(n + m), space: O(n + m)
# n = len(num1), m = len(num2)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        index1 = len(num1) - 1
        index2 = len(num2) - 1
        curt = 0
        while index1 >= 0 or index2 >= 0:
            if index1 >= 0:
                curt += int(num1[index1])
                index1 -= 1
            
            if index2 >= 0:
                curt += int(num2[index2])
                index2 -= 1
            
            res.append(str(curt % 10))
            curt //= 10
        
        if curt:
            res.append(str(curt))
            
        return ''.join(reversed(res))
