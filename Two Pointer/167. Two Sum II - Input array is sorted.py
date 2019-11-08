Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.



code:
Version 1: Two Pointer更优

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(numbers) - 1
        
        while start < end:
            if numbers[start] + numbers[end] == target:
            #注意题目的返回值，是第几个数，并且第一个数要小于第二个数
                return [start + 1, end + 1]
            if numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1
                
        return None
        
        
Version 2: Hash
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        
        for i in range(len(numbers)):
            if target - numbers[i] in hash:
                return [hash[target - numbers[i]] + 1, i + 1]
            hash[numbers[i]] = i
            
        return None
