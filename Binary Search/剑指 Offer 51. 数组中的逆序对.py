在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5
 

限制：

0 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# brute forceL TLE
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    res += 1
        
        return res

    
    
# merge sort
# time: O(nlogn), space: O(n)
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        temp = [0] * len(nums)

        return self.helper(nums, temp, 0, len(temp) - 1)
    
    def helper(self, nums, temp, start, end):
        if start >= end:
            return 0
        
        # 现在的nums为[start:mid] + [mid+1:end]，并且两段都为sorted
        mid = (start + end) // 2
        count = self.helper(nums, temp, start, mid) + self.helper(nums, temp, mid + 1, end)

        i, j, index = start, mid + 1, start
        while i <= mid and j <= end:
            # 若当前i的值小于j，则说明i比[mid+1:j-1]的值都大，因此把个数加入count
            if nums[i] <= nums[j]:
                temp[index] = nums[i]
                i += 1
                count += j - mid - 1
            else:
                temp[index] = nums[j]
                j += 1
            index += 1
        
        # 若i还有剩，则说明剩下的i都比[mid+1:end]大，即能构成逆序，此时end + 1 = j
        while i <= mid:
            temp[index] = nums[i]
            index += 1
            i += 1
            count += j - mid - 1

        while j <= end:
            temp[index] = nums[j]
            j += 1
            index += 1
        
        # 记得赋值
        nums[start:end+1] = temp[start:end+1]
        return count


