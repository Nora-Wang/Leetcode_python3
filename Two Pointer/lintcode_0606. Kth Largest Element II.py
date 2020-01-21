Find K-th largest element in an array. and N is much larger than k. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example

Example 1:

Input:[9,3,2,4,8],3
Output:4

Example 2:

Input:[1,2,3,4,5,6,8,9,10,7],10
Output:1

Notice

You can swap elements in the array


和215一模一样。。。。只是这道题的notice的意思就是用quick select的方法做题

code:
class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        if not nums or k < 1:
            return None
        
        return self.quick_select(nums, k, 0, len(nums) - 1)
        
    def quick_select(self, nums, k, start, end):
        if start >= end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[(start + end) // 2]
        
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            
            while left <= right and nums[right] < pivot:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        if start + k - 1 <= right:
            return self.quick_select(nums, k, start, right)
        
        if start + k - 1 >= left:
            return self.quick_select(nums, k - (left - start), left, end)

        return pivot
