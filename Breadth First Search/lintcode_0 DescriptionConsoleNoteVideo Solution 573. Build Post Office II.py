Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.

Return the smallest sum of distance. Return -1 if it is not possible.

Example

Example 1:

Input：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
Output：8
Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
Example 2:

Input：[[0,1,0],[1,0,1],[0,1,0]]
Output：4
Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
Notice

You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.


#Solution: from every house do BFS to count the distance from house to every empty place
#tricky points:
1. BFS的时候是分别对每个house进行一次BFS #一定要记得写visited，否则死循环
2. 对每个empty place都得记录一下一共有几个house能到达该点，因为题目要求所有house都能到达post
3. 在最后walk though数据的时候注意，有些点可能并不存在于house_count_record，即没有house能到达该点
#time: O(h * n * m), space: O(n * m). h = number of house, n * m = elements in grid
class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """

    def shortestDistance(self, grid):
        if not len(grid) or not len(grid[0]):
            return -1

        wall = set()
        house = set()
        queue = collections.deque()

        # find house and wall
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    house.add((i, j))
                if grid[i][j] == 2:
                    wall.add((i, j))

        # house many house can arrive curt empty place
        house_count_record = {}

        # count distance from every house to every empty place
        for x, y in house:
            self.bfs(grid, x, y, house, wall, house_count_record)

        # empty place + every house can arrive + min_distance
        res = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in house or (i, j) in wall or (i, j) not in house_count_record or house_count_record[(i, j)] != len(house):
                    continue

                res = min(res, grid[i][j])

        return res if res != float('inf') else -1

    def bfs(self, grid, x, y, house, wall, house_count_record):
        queue = collections.deque([(x, y)])
        visited = set()
        visited.add((x,y))

        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                if (x, y) not in house:
                    house_count_record[(x, y)] = house_count_record.get((x, y), 0) + 1

                for direct in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x_, y_ = direct[0] + x, direct[1] + y

                    if self.check(grid, x_, y_, wall, house, visited):
                        grid[x_][y_] += distance
                        queue.append((x_, y_))
                        visited.add((x_,y_))

        return

    def check(self, grid, x, y, wall, house, visited):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False

        if (x, y) in wall or (x, y) in house or (x, y) in visited:
            return False

        return True
