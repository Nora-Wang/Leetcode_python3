Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2


code:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(collections.Counter(nums).items(), key=lambda x:x[1])[-1][0]
