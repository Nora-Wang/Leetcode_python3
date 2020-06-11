Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:

Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        stack = []
        #从右往左数时，目前位置的最大值
        prev_max = -sys.maxsize
        
        for i in range(len(nums) - 1, -1, -1):
            #如果当前值小于之前的最大值时，证明132的1小于2，返回T
            if nums[i] < prev_max:
                return True
            
            #如果栈顶元素小于当前元素时，更新当前最大值到栈里，更新之前最大值（比当前最大值小一位）
            while stack and stack[-1] < nums[i]:
                prev_max = stack.pop()
            
            stack.append(nums[i])
            
        return False
        
