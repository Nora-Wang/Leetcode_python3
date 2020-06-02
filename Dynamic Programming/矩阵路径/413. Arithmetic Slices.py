A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.


code:
'''
if A[i] - A[i - 1] == A[i - 1] - A[i - 2] -> dp[i] = dp[i - 1] + 1
dp[i] means how many arithmetic slics end with A[i]

dp[2] = 1
dp[3] = dp[2] + 1 if match the rules
dp[4] = dp[3] + 1 if match the rules

return the sum of dp(don't know where to start and where to end)

time: O(n), space: O(n)
'''
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A:
            return 0
        
        dp = [0] * len(A)
        
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
        
        return sum(dp)
