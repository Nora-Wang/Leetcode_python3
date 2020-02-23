Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.


跟245是一类题,都是与index相关的list题目


code:
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        
        #对nums进行预处理,将不符合要求的都赋值为0
        #注意这里不能写for num in nums, num = 0,这样无法赋值
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > len(nums):
                nums[i] = 0
        
        #对nums进行处理
        for i in range(len(nums)):
            #为0,即不符合要求
            if nums[i] == 0:
                continue
            
            #<0证明这个index已经被处理了
            if nums[abs(nums[i]) - 1] < 0:
                continue
            
            #当该index的值为0时,赋值为-index+1,这样后面再访问该index时,会直接被当作<0处理
            if nums[abs(nums[i]) - 1] == 0:
                nums[abs(nums[i]) - 1] = -abs(nums[i])
                continue
            
            nums[abs(nums[i]) - 1] *= -1
        
        #当==0时,证明该点就是最小的那个值
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        
        #这里是所有的index都跑过了,即1~len(nums)都有了,因此返回值是len(nums) + 1
        return len(nums) + 1
        
