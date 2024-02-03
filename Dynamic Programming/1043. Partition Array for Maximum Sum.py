Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length


# https://leetcode.com/problems/partition-array-for-maximum-sum/discuss/290863/JavaC%2B%2BPython-DP-O(K)-Space
# dp[i] = max[dp[i], dp[i - sub_len] + max_value * sub_len
# Time O(nk), Space O(n)

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        l = len(arr)
        dp = [0] * (l + 1)
        
        for i in range(1, l + 1):
            cur_max = 0

            # 看本次的subarrays有多长
            for sub_len in range(1, k + 1):
                # 如果当前dp[i]都不够subarrays长度，那直接continue
                if i - sub_len < 0:
                    continue

                # 这里很巧妙，不是用的max(arr[i-sub_len:i])，而是越往后，前面的最大值也可能会被采用，因为anyway当前sub_len都是在k的范围内的
                # 但这里不能直接拿最大值，因为如果sub_len没有到k值，那后面大的值就没法拿到手，也就无法成为cur_max
                cur_max = max(cur_max, arr[i - sub_len])
                dp[i] = max(dp[i], dp[i - sub_len] + cur_max * sub_len)
        
        return dp[-1]
