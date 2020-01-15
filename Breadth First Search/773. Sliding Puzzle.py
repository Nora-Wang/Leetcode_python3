On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].



BFS题型
难点是判断queue中存储什么东西
这里的做法很牛逼,直接将整个board变为一个string,然后将string作为图中的node,然后通过找到string中的0,并将0和旁边的数字swap来得到一个新的string,
然后将新string push进queue继续循环;这样一次一次的比较,当被pop出来的string与target,即‘123450’,一样时,则停止



code:
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        if not board or not board[0]:
            return -1
        
        #得到初始string
        start = ''
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
        
        queue = collections.deque([start])
        visited = set([start])
        step = 0
        
        while queue:
            for _ in range(len(queue)):
                string = queue.popleft()
                if string == '123450':
                    return step
                
                #找到0在string中的index和在board中的i,j
                index, i, j = self.find_zero(string)
                
                #将0与周围4个点进行swap
                for d_i, d_j in [(0,1),(0,-1),(1,0),(-1,0)]:
                    new_i = i + d_i
                    new_j = j + d_j
                    #判断是否有意义
                    if self.is_valid(new_i, new_j):
                        #得到需要被swap的点在string中的index,然后进行swap
                        new_index = new_i * 3 + new_j
                        new_string = self.get_new_string(string, index, new_index)
                        
                        if new_string in visited:
                            continue
                        
                        queue.append(new_string)
                        visited.add(new_string)
                        
            #因为start string不算数,即这里要求的是边数,所以step被放在后面
            step += 1
        
        return -1
            
    
    def find_zero(self, string):
        for i in range(len(string)):
            if string[i] == '0':
                #数学问题
                return i, i / 3, i % 3
    
    def is_valid(self, i, j):
        #因为题目明确说了是一个2*3的board,所以直接用2,3即可
        return 0 <= i < 2 and 0 <= j < 3
    
    #swap的时候注意string是无法直接将两个值交换或者单独赋值的,所以需要list一下;同word ladder
    def get_new_string(self, string, index, new_index):
        list_str = list(string)
        list_str[index], list_str[new_index] = list_str[new_index], list_str[index]
        
        return ''.join(list_str)
