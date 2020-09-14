In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.



Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

|x| + |y| <= 300


code:
# BFS
DIRECTION = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        
        step = 0
        queue = collections.deque([(0,0,1)])
        visited = set([(0,0)])
        
        while queue:
            i, j, step = queue.popleft()

            for direct in DIRECTION:
                i_, j_ = i + direct[0], j + direct[1]

                if i_ == x and j_ == y:
                    return step

                if (i_,j_) in visited or abs(i_) + abs(j_) > 300:
                    continue

                queue.append((i_,j_,step + 1))
                visited.add((i_,j_))
        
