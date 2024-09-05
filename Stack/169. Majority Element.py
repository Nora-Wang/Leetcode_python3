Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2



# 2024/09/05
# Solutions:
# 1. hashmap      time O(n) space O(n)
# 2. map heapq    time O(n) space O(n)
# 3. sort         time O(nlogn) space O(1)
# 4. 摩尔选举      time O(n) space O(1)

# Hashmap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_map = collections.Counter(nums)

        # 3种return的方法
        # return max(nums_map, key=lambda num:nums_map[num])
        # return max(nums_map.items(), key=lambda x:x[1])[0]
        return max(nums_map, key=nums_map.get)


# Heap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_nums = collections.Counter(nums)
        # 1. Regular max heap
        heap = []
        for key, value in count.items():
            heap.append((-value, key))
        
        heapq.heapify(heap)
        
        return heapq.heappop(heap)[1]

        # 2. Use heapq.nlargest
        return heapq.nlargest(1, count_nums, key=count_nums.get)[0]


        

# Sort
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        
        count, result = 0, nums[0]
        i, j = 0, 0
        
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            
            
            gap = j - i
            if gap > count:
                result = nums[i]
                count = gap
            
            i = j
        
        return result


# 摩尔选举
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = 0
        count = 0
        
        for num in nums:
            if count == 0:
                cur = num
                
            if num == cur:
                count += 1
            else:
                count -= 1
        
        return cur












code:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(collections.Counter(nums).items(), key=lambda x:x[1])[-1][0]
    
    
#摩尔选举
#摩尔投票算法的基本原理关于摩尔投票算法的基本原理可以大致归纳为以下几步（为了方便理解，使用较为通俗语言进行描述）： 
# 1.  假设第一个数字是候选数字，计数为 1 。 
# 2.  遍历后面的数字，如果遇到相同的数字，计数加 1 ；如果遇到不同的数字，计数减 1 。 
# 3.  当计数减到0时，将当前数字设为新的候选数字，计数重新设为 1 。 
# 4.  最后剩下的候选数字很有可能是出现次数最多的数字。

# 作者：力扣（LeetCode）
# 链接：https://www.zhihu.com/question/49973163/answer/3202021480
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 完全按照上面解释的code
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if count == 0:
                cur = nums[i]
                count = 1
            elif nums[i] == cur:
                count += 1
            else:
                count -= 1
        
        return cur
        
# 简化后的code
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cur = 0
        
        for num in nums:
            if count == 0:
                cur = num
                
            if num == cur:
                count += 1
            else:
                count -= 1
        
        return cur
    
