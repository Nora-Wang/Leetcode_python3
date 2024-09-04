Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}



# 2024/09/04
# 快慢指针 time O(n), space O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not len(nums):
            return 0
        
        i, j = 0, 0
        
        while j < len(nums):
            while j < len(nums) and nums[j] == val:
                j += 1
            
            if j < len(nums):
                nums[i] = nums[j]
                j += 1
                i += 1
        
        return i



用相向双指针做

code:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        left, right = 0, len(nums) - 1
        
        #这里注意要=,因为这道题的结果是要求到最后的length,因此加=符号,最后left指的是第一个val值 = 前面所有非val值的length
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            
            while left <= right and nums[right] == val:
                right -= 1
        
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return left
