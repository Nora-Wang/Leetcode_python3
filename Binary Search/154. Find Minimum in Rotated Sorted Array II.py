Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?

# inner while loop去重法
# time: O(logn)(best case) ~ O(n)(worse case), space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            # 两个while loop直接将重复情况去掉
            while start + 1 < end and nums[start + 1] == nums[start]:
                start += 1
            while start + 1 < end and nums[end - 1] == nums[end]:
                end -= 1
            
            mid = (start + end) // 2
            
            # 只有一种情况是start = mid：在真的rotated的情况下（nums[start] >= nums[end]），nums[mid] >= nums[start]
            if nums[mid] >= nums[start] and nums[start] >= nums[end]:
                start = mid
            else:
                end = mid
        
        return nums[start] if nums[start] < nums[end] else nums[end]









# trick method
'''
第一次分类讨论：比较nums[start]和nums[end]

如果nums[left] < nums[right]，说明数组没有旋转过，仍然是升序排列。我们直接return nums[left]。
反之，说明数组非单调，进入到第二次分类讨论。

第二次分类讨论：比较nums[start]和nums[mid]，其中mid是二分中点。

如果nums[start] > nums[mid]，可以证明此时数组右半边是升序的（严格来说是非降序的），那我们就不用考虑右半边了。最小值一定在[start, mid]间，令end = mid
如果nums[start] < nums[mid]，可以证明此时数组左半边是升序的（同理，应为非降序），于是我们不需要考虑左半边。最小值一定在(mid, end]间，令start = mid
如果nums[start] == nums[mid]，是这道题区别于153的地方:
这时我们无法确定最小元素出现在哪里，举例来说，1,1,1,3,4和3,3,3,1,2，最左值和中间值都相等，最小值前者出现在左半边，后者出现在右半边。
所以我们无法进行二分，采用的方法是left += 1，可以证明这种做法不会使最小值丢失。然后在新的区间继续寻找。

参考：https://www.jiuzhang.com/problem/find-minimum-in-rotated-sorted-array-ii/#tag-lang-python
'''

# time: O(logn)(best case) ~ O(n)(worse case), space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            # 单增数组 -> 最小直接是start
            if nums[start] < nums[end]:
                return nums[start]
            
            mid = (start + end) // 2

            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[start]:
                end = mid
            else:
            # 与153最大的区别
            # 因为当前情况无法进行二分：case1 [3,3,3,1,3]; case2 [3,1,3,3,3]
            # nums[mid] == nums[start] -> min_num一定在[start + 1:end]之间，因此只是改变start的位置，以得到一个新的数组再进行判断
                start += 1
        
        return nums[start] if nums[start] < nums[end] else nums[end]
