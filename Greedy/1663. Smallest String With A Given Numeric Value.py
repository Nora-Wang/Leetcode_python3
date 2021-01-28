The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

 

Example 1:

Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.
Example 2:

Input: n = 5, k = 73
Output: "aaszz"
 

Constraints:

1 <= n <= 105
n <= k <= 26 * n


# 从后往前放，先尽量放z，然后除了一位，其余部分全部放a -> 实现最小
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = []
        
        z_count = k // 26
        rest_count = k % 26
        
        # 当剩余部分用a填仍然不足时，则需要退一位z以做补充
        while rest_count + z_count < n:
            z_count -= 1
            rest_count += 26
        
        res.append(z_count * 'z')
        a_count = n - z_count - 1
        if a_count >= 0:
            res.append(chr(ord('a') + rest_count - a_count - 1))
            res.append(a_count * 'a')
        
        return ''.join(reversed(res))
