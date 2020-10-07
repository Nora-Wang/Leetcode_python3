Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0


code:
'''
本题中，我们需要得到m,n所有元素按位与的结果。
举个例子，当m=26，n=30时，它们的二进制表示为为： 11010　　11011　　11100　　11101　　11110 这个样例的答案是11000，易见我们发现我们只需要找到m和n最左边的公共部分即可。
'''
# time: O(1), space: O(1)
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        
        while m != n:
            m >>= 1
            n >>= 1
            shift += 1
        
        return n << shift
