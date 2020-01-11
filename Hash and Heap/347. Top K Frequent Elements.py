Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


code:
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        #遍历一遍数组,记录每个number出现的次数
        record = {}
        for i in nums:
            record[i] = record.get(i, 0) + 1
            
        #根据哈希表的value,即每个number出现的次数,来排序,再反转(value最大的放前面)
        #注意sorted后的结果为list
        #这里的结果为[[key, value]],key是number的值,value是number出现的次数,因此后续取值时是sorted_nums[i][0]
        sorted_nums = sorted(record.items(), key = lambda item:item[1], reverse = True)    
        
        #得到前k个数的值
        result = []
        for i in range(k):
            result.append(sorted_nums[i][0])
        
        return result
            
        
