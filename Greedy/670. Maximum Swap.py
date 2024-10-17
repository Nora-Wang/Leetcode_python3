You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108

4 steps with explanation:
https://leetcode.com/problems/maximum-swap/discuss/846837/Python-3-or-Greedy-Math-or-Explanations

Time O(n), Space O(n)
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        n = len(num)
        
        # 1. find the first increasing digit with index - the flip one
        index = 0
        for i in range(1, n):
            # Tips: int(num[i]) == int(num[i - 1]) case should continually moving index
            # Sample input 9982
            if int(num[i]) > int(num[i - 1]):
                index = i - 1
                break
                
        # 2. find the farthest max digit with max_index in num[index:] - the right swap one
        max_index = index
        for i in range(index, n):
            # Tips: should be the farthest one
            # Sample input 1993, if not the farthest one, the wrong result will be 9193
            if int(num[i]) >= int(num[max_index]):
                max_index = i
                
        # 3. find the farthest digit in num[:index] which is smaller than num[max_index] - the left swap one
        # because the left side digits of index, num[:index], should be decreasing
        min_index = index
        for i in range(index, -1, -1):
            # Tips: should be the farthest one
            # Sample input 2299, if not the farthest one, the wrong result will be 2992
            if int(num[max_index]) > int(num[i]):
                min_index = i
        
        # 4. swap
        # Tips: if no swap, max_index shoule be the same as min_index
        num[max_index], num[min_index] = num[min_index], num[max_index]
        
        return int(''.join(num))
