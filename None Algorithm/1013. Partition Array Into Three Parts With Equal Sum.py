Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

 

Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

Constraints:

3 <= arr.length <= 5 * 104
-104 <= arr[i] <= 104


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3:
            return False
        
        target = sum(arr) // 3
        
        i = 1
        curt_i = arr[0]
        while i < len(arr) and curt_i != target:
            curt_i += arr[i]
            i += 1
        
        curt_j = arr[len(arr) - 1]
        j = len(arr) - 2
        while j >= 0 and curt_j != target:
            curt_j += arr[j]
            j -= 1
            
        return i <= j and curt_i == curt_j == target == sum(arr[i:j+1])
        
        
        
        
        
