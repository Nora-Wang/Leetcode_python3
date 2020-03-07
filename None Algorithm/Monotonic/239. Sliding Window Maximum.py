Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?


code:
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        if k > len(nums):
            k = len(nums)
        
        queue = collections.deque()
        
        for i in range(k):
        #利用deque的特性:把nums[i]放到queue里面的时候,如果发现前面的值比nums[i]小,就将前面的值pop;如果大就把nums[i]放它后面
        #这样就能保证前面的值一定比后面的值大,从而形成一个单调queue
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)
        
        result = []
        result.append(nums[queue[0]])
        
        for i in range(len(nums) - k):
            while queue and nums[queue[-1]] < nums[i + k]:
                queue.pop()
            
            queue.append(i + k)
            
            #如果pop的值是此时的最大值,则需要popleft,从而保证queue[0]始终为当前的最大值
            if i == queue[0]:
                queue.popleft()
            
            result.append(nums[queue[0]])
        
        return result
