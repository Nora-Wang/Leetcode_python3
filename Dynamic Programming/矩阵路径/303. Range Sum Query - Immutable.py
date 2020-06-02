Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:

You may assume that the array does not change.
There are many calls to sumRange function.


code:
class NumArray:

    def __init__(self, nums: List[int]):
        record = 0
        for i in range(len(nums)):
            nums[i] += record
            record = nums[i]
        
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j] - self.nums[i - 1] if i else self.nums[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
