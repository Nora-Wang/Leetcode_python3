You are given two 32-bit numbers, N and M, and two bit positions, i and j Write a method to set all bits between i and j in N equal to M 
(e g , M becomes a substring of N located at i and starting at j)

EXAMPLE:
Input: N = 10000000000, M = 10101, i = 2, j = 6 Output: N = 10001010100

# time: O(n), space: O(1)
def solution(n, m, i, j):
    # deal m -> 0000[m]0*i
    m = m << i

    # deal n -> nnnn[0*m]nnnn
    for move in range(i, j + 1):
        n = n & (~(1 << move))

    res = n | m
    return res

n = int('10000000000', 2)
m = int('10101', 2)
i = 2
j = 6
print(int('10001010100', 2))
print(solution(n, m, i, j))
    
