Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible..

Students must be placed in seats in good condition.

 

Example 1:


Input: seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
Output: 4
Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam. 
Example 2:

Input: seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
Output: 3
Explanation: Place all students in available seats. 

Example 3:

Input: seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
Output: 10
Explanation: Place students in available seats in column 1, 3 and 5.
 

Constraints:

seats contains only characters '.' and'#'.
m == seats.length
n == seats[i].length
1 <= m <= 8
1 <= n <= 8



code:
DIRECITONS = [(0,1),(0,-1),(-1,1),(-1,-1),(1,-1),(1,1)]
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        if not len(seats) or not len(seats[0]):
            return 0
        
        self.count = 0
        list = []
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] == '.':
                    list.append((i,j))
                    
        self.dfs(seats, 0, 0, list, 0, [])
        
        return self.count
    
    def dfs(self, seats, temp_count, step, list, index, visited):
        if step == len(list):
            #print(temp_count)
            self.count = max(self.count, temp_count)
            return
        
        for k in range(index, len(list)):
            #print(list[k])
            i, j = list[k][0], list[k][1]
            if (i,j) in visited:
                self.dfs(seats, temp_count, step + 1, list, index + 1, visited)
                continue
            
            s_l = 1
            visited.append((i,j))
            for direct in DIRECITONS:
                x_ = i + direct[0]
                y_ = j + direct[1]
                
                if 0 <= x_ < len(seats) and 0 <= y_ < len(seats[0]) and (x_, y_) not in visited and seats[x_][y_] == '.':
                    s_l += 1
                    visited.append((x_,y_))
            
            #print(visited)
            #print(temp_count)
            #print(step)
            self.count = max(self.count, temp_count)
            self.dfs(seats, temp_count + 1, step + 1, list, index + 1, visited)
            
            
            while s_l:
                visited.pop()
                s_l -= 1
        
        
        
        
        
