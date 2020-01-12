Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the terminating number arrives. If the unique number is not found, return -1.

Example

Example1

Input: 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
5
Output: 3
Example2

Input: 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
7
Output: -1
Example3

Input: 
[1, 2, 2, 1, 3, 4]
3
Output: 3

题目的意思是在nums中,找number前(包括number)的数据中unique的那个


code:
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        if not nums:
            return -1
        
        record = {}
        for i in range(len(nums)):
            record[nums[i]] = record.get(nums[i], 0) + 1
            if  nums[i] == number:
                break
        
        if nums[i] != number:
            return -1
        
        for item in nums:
            if record[item] == 1:
                return item
            
        return -1
