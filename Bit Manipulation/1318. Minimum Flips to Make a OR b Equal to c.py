Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

Example 1:



Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0
 

Constraints:

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9



这题思考了一下，只能一个bit一个bit的去判断，因为存在两个case是
1. a = 0, b = 1, c = 0
2. a = 1, b = 1, c = 0
这里a | b ^ c都是1，但第一种case只用改b的值就可以，而第二种case是需要同时更改a和b


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        
        while c:
            a_value = a & 1
            b_value = b & 1
            c_value = c & 1
            
            isDiff = a_value | b_value != c_value
            count += 1 if isDiff else 0
            if a_value and b_value and isDiff:
                count += 1
            
            a >>= 1
            b >>= 1
            c >>= 1

        # After checked all the bits in c, but for a and b, they may still have 1 bit in any other positions
        if a:
            count += bin(a).count('1')
        if b:
            count += bin(b).count('1')
        
        return count


# code optimize
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        
        while a or b or c:
            a_value = a & 1
            b_value = b & 1
            c_value = c & 1
            
            if a_value | b_value != c_value:
                if not c_value:
                    count += a_value + b_value
                else:
                    count += 1
            
            a >>= 1
            b >>= 1
            c >>= 1
        
        return count
