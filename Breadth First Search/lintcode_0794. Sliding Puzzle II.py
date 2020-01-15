On a 3x3 board, there are 8 tiles represented by the integers 1 through 8, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

Given an initial state of the puzzle board and final state, return the least number of moves required so that the initial state to final state.

If it is impossible to move from initial state to final state, return -1.

Example

Example 1:

Input:
[
 [2,8,3],
 [1,0,4],
 [7,6,5]
]
[
 [1,2,3],
 [8,0,4],
 [7,6,5]
]
Output:
4

Explanation:
[                 [
 [2,8,3],          [2,0,3],
 [1,0,4],   -->    [1,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [2,0,3],          [0,2,3],
 [1,8,4],   -->    [1,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [0,2,3],          [1,2,3],
 [1,8,4],   -->    [0,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [1,2,3],          [1,2,3],
 [0,8,4],   -->    [8,0,4],
 [7,6,5]           [7,6,5]
]                 ]
Example 2：

Input:
[[2,3,8],[7,0,5],[1,6,4]]
[[1,2,3],[8,0,4],[7,6,5]]
Output:
-1
Challenge

How to optimize the memory?
Can you solve it with A* algorithm?


跟leetcode 773一样,只是board多了一行,这只会导致换算string中的index的数据变一下,其他的都一样

code:
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        if not init_state or not init_state[0]:
            return -1
        
        start, end = '', ''
        for i in range(len(init_state)):
            for j in range(len(init_state[0])):
                start += str(init_state[i][j])
                end += str(final_state[i][j])
        
        queue = collections.deque([start])
        visited = set([start])
        step = 0
        
        while queue:
            for _ in range(len(queue)):
                string = queue.popleft()
                if string == end:
                    return step
                
                index, i, j = self.find_zero(string)
                
                for direct in [(0,1),(0,-1),(1,0),(-1,0)]:
                    new_i = i + direct[0]
                    new_j = j + direct[1]
                    
                    if self.is_valid(new_i, new_j):
                        new_index = new_i * 3 + new_j
                        new_string = self.get_new_string(string, index, new_index)
                        
                        if new_string in visited:
                            continue
                        
                        queue.append(new_string)
                        visited.add(new_string)
            
            step += 1
            
        return -1
            
    def find_zero(self, string):
        for i in range(len(string)):
            if string[i] == '0':
                return i, i / 3, i % 3
                
                
    def is_valid(self, i, j):
        return 0 <= i < 3 and 0 <= j < 3
        
    def get_new_string(self, string, index, new_index):
        list_str = list(string)
        list_str[index], list_str[new_index] = list_str[new_index], list_str[index]
        return ''.join(list_str)
