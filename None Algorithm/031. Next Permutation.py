Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        # 找到第一个比后面数要小的数的index
        index = len(nums) - 2
        while index >= 0 and nums[index] >= nums[index + 1]:
            index -= 1
        
        # nums单调递减的情况
        if index == -1:
            nums.sort()
            return
        
        # 在后面的数中找到与nums[index]最近且更大的数
        swap_index = len(nums) - 1
        while nums[swap_index] <= nums[index]:
            swap_index -= 1
        nums[swap_index], nums[index] = nums[index], nums[swap_index]
        
        # 将index之后的数据进行排序（这部分的数据应为单减的，因此直接头尾swap即可）
        left, right = index + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return






code:
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #倒着找，找到第一个前数小于后数（递增）的数，前数位置为i 
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        #如果可以循环完，证明整个数组为降序，反转全部 
        else:
            nums.reverse()
            return
        
        #倒着找，找到第一个大于nums[i]的数，交换位置   
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                break
        
        #反转i之后的所有数 
        for j in range(0, (len(nums) - i) // 2):
            nums[i+j+1], nums[len(nums)-j-1] = nums[len(nums)-j-1], nums[i+j+1]
        
        return
