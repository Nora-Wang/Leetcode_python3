Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.




思路:
将nums变为set,对每个nums中的每个数字,向左向右搜一下,看最长能有多长 
还有就是,如果4向左向右搜到了1 2 3,那么1 2 3这三个数字就不用向左向右搜了(发现冗余),即直接将1 2 3从nums_set中remove掉


code:
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        #dict需要for循环初始化,set直接set()即可
        nums_set = set(nums)

        result = 0
        for item in nums:
            count = 1
            #这里一定要对item进行记录,因为在往右搜索时,item会变;即到下一个while循环时,item已经被改变
            #或者直接用item_up = item + 1和item_down = item - 1进行记录,这样在每次while循环中调用的是item_up和item_down,在相互之间不会影响
            recode = item
            while item + 1 in nums_set:
                #dict删除用del,set、list删除用remove,queue删除用popleft,stack(用list实现)删除用pop
                nums_set.remove(item + 1)
                item += 1
                count += 1
                
            item = record
            while item - 1 in nums_set:
                nums_set.remove(item - 1)
                item -= 1
                count += 1
            
            #要取最大值
            result = max(result, count)
            
        return result
