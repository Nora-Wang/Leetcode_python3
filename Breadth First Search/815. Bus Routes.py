We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Note:

1 <= routes.length <= 500.
1 <= routes[i].length <= 500.
0 <= routes[i][j] < 10 ^ 6.

#超时做法
code:
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        
        #hash_r[stop] = [next_stops]
        hash_r = collections.defaultdict(list)
        for row in routes:
            for i in range(len(row) - 1):
                for j in range(i + 1, len(row)):
                    hash_r[row[i]].append(row[j])
                    hash_r[row[j]].append(row[i])
        
        
        #每一层存储当前stop可以到达的next_stops
        queue = collections.deque([S])
        visited = set()
        count = 0
        
        while queue:
            count += 1
            for _ in range(len(queue)):
                stop = queue.popleft()
                visited.add(stop)
                
                for next_stop in hash_r[stop]:
                    if next_stop == T:
                        return count
                    
                    if next_stop not in visited:
                        queue.append(next_stop)
        
        return -1
