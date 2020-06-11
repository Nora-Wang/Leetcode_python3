Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1

#没有直接用到单调栈，但用到了单调栈的思想
#https://www.youtube.com/watch?v=OKNpknDO86U

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        #nums = [int(c) for c in str(n)]
        n_list = list(map(int, str(n)))
        
        #from right to left, find first digit that's smaller than its next digit
        i = len(n_list) - 1
        while i > 0 and n_list[i - 1] >= n_list[i]:
            i -= 1
        
        #descending order corner case
        if i == 0: return -1
        
        #因为在找i的时候就使得n_list[i:]一定是descending order，因此直接reverse即可
        n_list[i:] = reversed(n_list[i:])
        
        #in n_list[i:], find the first digit that's larger that n_list[i - 1]
        j = i
        while j < len(n_list) and n_list[j] <= n_list[i - 1]:
            j += 1
        
        n_list[j], n_list[i - 1] = n_list[i - 1], n_list[j]
        
        res = int(''.join(map(str, n_list)))
        
        #判断res有没有超过32位整数的最大值
        return res if res <= (1 << 32 - 1) else -1
