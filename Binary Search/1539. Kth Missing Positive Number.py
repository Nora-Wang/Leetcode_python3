Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length


# Brute force
# time: O(n)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 1
        for num in arr:
            if num - prev >= k:
                return prev + k - 1
            k -= num - prev
            prev = num + 1
        
        return prev + k - 1
        
        
        
        
# Binary Search
# Reference: https://leetcode.com/problems/kth-missing-positive-number/discuss/779999/JavaC%2B%2BPython-O(logN)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1
        
        return left + k
