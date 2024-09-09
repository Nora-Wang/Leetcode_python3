You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

 

Example 1:


Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:


Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
 

Constraints:

1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000



# 逻辑要想清楚，不需要用level啥的多此一举的去加减得到i,j，直接set出topRow、bottonRow、leftCol、rightCol

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1] * n for _ in range(m)]
        topRow, bottonRow = 0, m - 1
        leftCol, rightCol = 0, n - 1
        
        while head:
            # Top Row
            for col in range(leftCol, rightCol + 1):
                if not head:
                    break
                result[topRow][col] = head.val
                head = head.next
            topRow += 1
            
            # Right Column
            for row in range(topRow, bottonRow + 1):
                if not head:
                    break
                result[row][rightCol] = head.val
                head = head.next
            rightCol -= 1
            
            # Botton Row
            for col in range(rightCol, leftCol - 1, -1):
                if not head:
                    break
                result[bottonRow][col] = head.val
                head = head.next
            bottonRow -= 1
                
            # Left Column
            for row in range(bottonRow, topRow - 1, -1):
                if not head:
                    break
                result[row][leftCol] = head.val
                head = head.next
            leftCol += 1
        
        return result
            
            
