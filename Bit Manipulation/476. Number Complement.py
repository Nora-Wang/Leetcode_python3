The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

1 <= num < 231
 

Note: This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/


Solution 1:
参考link: https://leetcode.com/problems/number-complement/discuss/5671548/100.0Easy-SolutionWith-Explanation
class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()
        
        helper = (1 << bit_length) - 1
        
        return num ^ helper


Solution 2:
class Solution:
    def findComplement(self, num: int) -> int:
        return int((bin(num)[2:]).replace("1", "2").replace("0", "1").replace("2", "0"),2)


Solution 3:
class Solution:
    def findComplement(self, num: int) -> int:
        list_num = list(bin(num))
        res = []
        
        for val in list_num[2:]:
            res.append("1" if val == "0" else "0")
        
        return int(''.join(res), 2)

 class Solution:
    def findComplement(self, num: int) -> int:
        str_num = bin(num)
        res = []
        
        for i in range(2, len(str_num)):
            res.append("1" if str_num[i] == "0" else "0")
        
        return int(''.join(res), 2)
