Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 

Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8



code:
'''
1. brute force 1
traverse all elements in the range [nums[0], nums[-1] + 1]
A -> set_A
while k:
    if curt num in set_A -> continue
    if curt num not in set_A -> missing number -> res = curt num
time: O(n), space: O(n)

2. brute force 2
traverse all elements in the nums, calculate how many missing number between nums[i] and nums[i - 1] -> count
if count < k -> renew k -> k -= count
if count >= k -> res = nums[i - 1] + k

3. binary search
calculate how many missing number between nums[start] and nums[mid] -> count
if count < k -> start = mid, k -= count
if count >= k -> end = mid
attention: if count == k -> end = mid (because we need to find the leftmost number)

in the end: 
if count between nums[start] and nums[end] >= k -> nums[start] += k
else: nums[end] += k

time: O(logn), space: O(1)
'''
# brute force 2
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            count = nums[i] - nums[i - 1] - 1
            
            if count >= k:
                return nums[i - 1] + k
                
            k -= count
        
        return nums[-1] + k

# binary search
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            miss_count = (nums[mid] - nums[start] - 1) - (mid - start - 1)
            
            if miss_count < k:
                start = mid
                k -= miss_count
            else:
                end = mid
        
        miss_count_start_end = nums[end] - nums[start] - 1
        if miss_count_start_end >= k:
            return nums[start] + k
        return nums[end] + k - miss_count_start_end
