Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example

Example 1:

Input:
[],9
Output:
0

Example 2:

Input:
[3,2,2,1],2
Output:1
Explanation:
the real array is[1,2,2,3].So return 1
Challenge

Can you partition the array in-place and in O(n)?

Notice

You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length



这道题的主要思路就是quick sort，但注意区别与quick sort的不同点，理解为什么


code:
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        if not nums:
            return 0
            
        start, end = 0, len(nums) - 1
        
        #这里要用<=
        #因为用<时，跳出while循环时，最后的那个值不知道应该放在k左侧还是右侧，因此在最后需要另加判断以k的大小比较来确定位置
        #而用<=,则可以省略这一步
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
                
            与quick sort的不同点
            #quick sort中：while start <= end and nums[end] > k:
            #quick sort如果有等号，则会stack overflow，当array中所有值都一样时
            #quick sort中等号情况不做分析，因此unstable
            
            #这道题是题目中说了All elements >= k are moved to the right，因此有等号
            while start <= end and nums[end] >= k:
                end -= 1
            
            #找到一个不应该在左侧和一个不应该在右侧的值，swap them
            if start <= end:
                nums[start], nums[end] = nums[end], n[start]
                start += 1
                end -= 1
                
        return start
