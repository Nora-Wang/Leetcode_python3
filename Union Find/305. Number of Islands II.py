A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?




code:
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        result = []
        #把访问过的岛存入island;注意只有访问过的岛,其值才为1
        visited = set()
        #union-find需要一个哈希father
        self.father = {}
        self.size = 0
        
        #遍历每一个点 
        for x,y in positions:
            #如果该点被访问过,即代表该点是之前被访问的(new_x,new_y)中的一员,因此数目不变,直接加入结果 
            if (x,y) in visited:
                result.append(self.size)
                continue
            
            #如果没被访问过,先加入visited,再把当前点的父节点设置为自己(根),数目加一 
            visited.add((x,y))
            self.father[(x,y)] = (x,y)
            self.size += 1
            
            #向4个方向找有没有连通的岛屿
            for direct in DIRECTIONS:
                new_x = x + direct[0]
                new_y = y + direct[1]
                #如果某方向存在联通的岛屿,需要做并查集 
                #这里的判断条件是因为只有访问过的岛,其值才为1,即存在于visited的点才是岛,否则就是海
                if (new_x,new_y) in visited:
                    self.union((x,y),(new_x,new_y))
                    
            #添加当前size        
            result.append(self.size)
                
        return result
    
    #Union set
    def union(self, point_a, point_b):
        #找到两个元素的根（顶端）
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        
        #如果根不是同一个，把a接到b上，size减小1 
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size -= 1
    
    #Find set + Compressed path
    def find(self, point):
        path = []
        
        while self.father[point] != point:
            path.append(point)
            point = self.father[point]
        
        for p in path:
            self.father[p] = point
        
        return point
