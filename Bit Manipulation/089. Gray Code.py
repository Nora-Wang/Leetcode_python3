The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
             
             

# The middle two numbers only differ at their highest bit, while the rest numbers of part two are exactly symmetric of part one.
# Input is 2:
# 00
# 01
# 11
# 10

# Input is 3:
# 0 000
# 1 001
# 3 011
# 2 010

# 6 110
# 7 111
# 5 101
# 4 100

# For the pair of (2, 6), (3, 7), (1, 5) and (0, 4), the last 2 bits are the same. The only difference is 6,7,5 and 4 set the first bit on. Hope this helps.


# Backtracking Version
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        
        self.helper(n, res)
        
        return res
    
    def helper(self, n, res):
        # base case
        if n == 0:
            res.append(0)
            return res
        
        # 先拿到n - 1的res
        self.helper(n - 1, res)
        
        # 将n - 1的res的第n - 1加入1 -> 得到n的res
        move = 1 << (n - 1)
        for i in range(len(res) - 1, -1, -1):
            res.append(res[i] | move)
             
             
             
# Non-recursion Version
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | (1 << i))
        
        return res
