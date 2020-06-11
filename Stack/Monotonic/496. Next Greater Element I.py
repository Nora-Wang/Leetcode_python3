You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:

All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

#06/11/2020
#一开始理解错题意了，浪费了好多时间，太傻逼了。。难点在于判断出需要用到单调递减的单调栈
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        
        if not nums2:
            return [-1] * len(nums1)
        
        stack = []
        record = {}
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                record[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            
            stack.append(i)
        
        res = []
        for num in nums1:
            if num in record:
                res.append(record[num])
            else:
                res.append(-1)
        
        return res



单调栈问题

code:
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record = {}
        #单调栈模板
        
        stack = []
        
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                #为了方便后续查找,这里用hash table记录结果
                record[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            
            stack.append(i)
        
        results = []
        
        #hash table的结果是,若后续有比num大的数,则记录在value中,若没有,则不存在于hash table中
        for num in nums1:
            if num not in record:
                results.append(-1)
                continue
                
            results.append(record[num])
        
        return results
