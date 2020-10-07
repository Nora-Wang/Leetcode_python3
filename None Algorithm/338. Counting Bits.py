Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.


# Version 1
# time: O(n*sizeof(integer)), space: O(1)
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            count = self.get_count(i)
            res.append(count)
        
        return res
    
    def get_count(self, num):
        count = 0
        while num != 0:
            if (num & 1) == 1:
                count += 1
            
            num = num >> 1
        
        return count
        
# Version 2
# time: O(n), space: O(1)
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + i % 2
        
        return dp
