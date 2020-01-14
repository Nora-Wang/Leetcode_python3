Given an array and a window size that is sliding along the array, find the sum of the count of unique elements in each window.

Example

Example1

Input:
[1, 2, 1, 3, 3]
3
Output: 5
Explanation:
First window [1, 2, 1], only 2 is unique, count is 1.
Second window [2, 1, 3], all elements unique, count is 3.
Third window [1, 3, 3], only 1 is unique, count is 1.
sum of count = 1 + 3 + 1 = 5
Example1

Input:
[1, 2, 1, 2, 1]
3
Output: 3
Notice

If the window size is larger than the length of array, just regard it as the length of the array (i.e., the window won't slide).


sliding window题目

code:
class Solution:
    """
    @param nums: the given array
    @param k: the window size
    @return: the sum of the count of unique elements in each window
    """
    def slidingWindowUniqueElementsSum(self, nums, k):
        #重点！！！！
        if k > len(nums):
            k = len(nums)
        
        record = {}
        for i in range(k):
            record[nums[i]] = record.get(nums[i], 0) + 1
        
        result = 0
        for num in record:
            if record[num] == 1:
                result += 1
            
        count = result
        
        for i in range(len(nums) - k):
            #把头给删除,当发现出现次数是从1变为0时,则需要将其从count中减去;当发现出现次数是从0变为1时,则需要将其加入count
            record[nums[i]] -= 1
            if record[nums[i]] == 0:
                count -= 1
            if record[nums[i]] == 1:
                count += 1
            
            #把尾给新加一个数,当发现出现次数是从1变为2时,则需要将其从count中减去;当发现出现次数是从0变为1时,则需要将其加入count
            record[nums[i + k]] = record.get(nums[i + k], 0) + 1
            if record[nums[i + k]] == 1:
                count += 1
            if record[nums[i + k]] == 2:
                count -= 1
            
            result += count
        
        return result
