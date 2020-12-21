Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]
 

Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000


# from Link: https://leetcode.com/problems/smallest-range-ii/discuss/173377/C%2B%2BJavaPython-Add-0-or-2-*-K
Intuition:

For each integer A[i],
we may choose either x = -K or x = K.

If we add K to all B[i], the result won't change.

It's the same as:
For each integer A[i], we may choose either x = 0 or x = 2 * K.

Explanation:

We sort the A first, and we choose to add x = 0 to all A[i].
Now we have res = A[n - 1] - A[0].
Starting from the smallest of A, we add 2 * K to A[i],
hoping this process will reduce the difference.

Update the new mx = max(mx, A[i] + 2 * K)
Update the new mn = min(A[i + 1], A[0] + 2 * K) 
# 这里之所以是A[0] + 2 * K，是因为我们的目的是让diff更小，当A[i]加了2K之后，一定是A[0]也同时加上2K才会得到更小的diff
# 这里是所以跟A[i + 1]做比较是因为对于A[:i+1]的数据我们已经加上了2K，因此最小的数据一定是min（A[0] + 2K的结果，A[i + 1]不加上2K(A[i + 1]自己)的结果）
Update the res = min(res, mx - mn)

Time Complexity:

O(NlogN), in both of the worst and the best cases.
In the Extending Reading part, I improve this to O(N) in half of cases.


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        res = A[-1] - A[0]
        
        for i in range(len(A) - 1):
            big = max(A[i] + 2 * K, A[-1])
            small = min(A[0] + 2 * K, A[i + 1])
            
            res = min(res, big - small)
        
        return res
