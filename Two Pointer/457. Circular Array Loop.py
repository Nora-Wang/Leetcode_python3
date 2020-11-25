You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.

 

Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
Example 2:

Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.
Example 3:

Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.
 

Note:

-1000 ≤ nums[i] ≤ 1000
nums[i] ≠ 0
1 ≤ nums.length ≤ 5000
 

Follow up:

Could you solve it in O(n) time complexity and O(1) extra space complexity?


# 其实类似LinkedList里的快慢指针找cycle entrance
# Leetcode 141/142

# 两个while中 '> 0' 的设计很tricky
# 因为这样写既能保证下一步的direction与nums[i]相同，又能保证下一步的值不为0
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        n_len = len(nums)
        
        for i in range(n_len):
            if nums[i] == 0:
                continue
                
            slow, fast = i, self.get_index(nums, i)
            
            # 因为slow肯定能valid，因此只要判断fast即可
            # equals to while fast and fast.next are valid （类似LinkedList）
            while nums[i] * nums[fast] > 0 and nums[i] * nums[self.get_index(nums, fast)] > 0:
                if slow == fast:
                    # edge case: 1 length cycle
                    if slow == self.get_index(nums, slow):
                        break
                    return True
                slow = self.get_index(nums, slow)
                fast = self.get_index(nums, self.get_index(nums, fast))
            
            # mark all the path_elements to 0
            # path: i to end; end is when nums[slow] reverse direction or nums[slow] == 0
            slow = i
            direction = nums[i]
            while direction * nums[slow] > 0:
                slow_next = self.get_index(nums, slow)
                nums[slow] = 0
                slow = slow_next
        
        return False
            
    
    def get_index(self, nums, i):
        index = i
        if nums[i] < 0:
            index += len(nums)
        
        return (index + nums[i]) % len(nums)
