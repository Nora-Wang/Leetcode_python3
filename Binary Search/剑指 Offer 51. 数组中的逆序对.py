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

    
    
# insert sort + binary search
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_prefix = [nums[0]] # decreasing
        res = 0

        for i in range(1, len(nums)):
            # find first element <= nums[i]
            index = self.find(sorted_prefix, nums[i])
            res += index
            sorted_prefix.insert(index, nums[i])
        
        return res

    def find(self, sorted_prefix, num):
        if num >= sorted_prefix[0]:
            return 0
        if num < sorted_prefix[-1]:
            return len(sorted_prefix)

        start, end = 0, len(sorted_prefix) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if sorted_prefix[mid] <= num:
                end = mid
            else:
                start = mid
        
        return start if sorted_prefix[start] <= num else end

