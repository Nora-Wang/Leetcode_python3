Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}


# 1/24/21
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow, quick = 0, 0
        
        while quick < len(nums):
            count = 1
            while quick + 1 < len(nums) and nums[quick + 1] == nums[quick]:
                quick += 1
                count += 1
            
            if count >= 2:
                nums[slow] = nums[quick]
                nums[slow + 1] = nums[quick]
                slow += 2
            else:
                nums[slow] = nums[quick]
                slow += 1
            
            quick += 1
        
        return slow







# 12/11/2020
# time: O(n), space: O(1)
# slow: the last valid number -> valid nums: nums[:slow+1]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        slow, fast = 1, 2
        while fast < len(nums):
            if nums[slow] != nums[fast] or (nums[slow] == nums[fast] and nums[slow] != nums[slow - 1]):
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        
        return slow + 1
    

    
    



two pointer
时间O(n), 空间O(1)

code:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        slow = 0
        count = 1
        
        for fast in range(1, len(nums)):
            #计算count
            if nums[slow] == nums[fast]:
                count += 1
            else:
                count = 1
            
            #这样写可以把重复的情况也包括在内
            if count <= 2:
                slow += 1
                nums[slow] = nums[fast]
                
        
        return slow + 1
                
