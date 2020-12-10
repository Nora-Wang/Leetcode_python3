Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^4


'''
two pointer
left, right = 1, len(arr) - 2

while left keep on increasing: left++ -> get the peek for left
while right keep on decreasing: right-- -> get the peek for right
only if left == right -> True
edge case: Monotonic stack. [3,4,5], False -> left != len(arr) - 1 and right != 0
time: O(n), space: O(1)
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        left, right = 0, len(arr) - 1
        
        while left < len(arr) - 1 and arr[left] < arr[left + 1]:
            left += 1
        while right > 1 and arr[right - 1] > arr[right]:
            right -= 1
        
        # when left == right -> left and right reach the peek
        # left != len(arr) - 1 and right != 0 -> edge case: Monotonic stack
        return left == right and left != len(arr) - 1 and right != 0
