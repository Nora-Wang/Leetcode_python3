Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:

The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].




code:
#对每个num进行遍历,看num - k是否在hash table中
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums or k < 0:
            return 0
        
        hash_nums = collections.Counter(nums)
        
        count = 0
        
        for num in hash_nums:
            if k == 0:
                if hash_nums[num] > 1:
                    count += 1
            else:
                if num - k in hash_nums:
                    count += 1
        
        return count
    
    
    
    
    
    
#用hash记录每个值出现的次数,若k为0,则count=所有出现次数>1的数;否则,判断num -/+ k在不在hash表中,注意最后结果需要除以2
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        #注意corner case:k<0
        if not nums or k < 0:
            return 0
        
        record = {}
        
        for num in nums:
            record[num] = record.get(num, 0) + 1
        
        count = 0
        
        for num in record:
            #注意这里的if判断的写法
            if k == 0:
                if record[num] > 1:
                    count += 1
                    continue
            else:
                if num + k in record:
                    count += 1
                if num - k in record:
                    count += 1

        if k == 0:
            return count
        #k不为0时,count要除以2,因为pair中的两个数被分别算了一次,即被重复计算
        return count // 2
