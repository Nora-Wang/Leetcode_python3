题目：
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1



# BFS
# time: O(V + E), space: O(V)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        
        # graph = {node:[neighbors]}
        graph = {}
        for i in range(n):
            graph[i] = []
        for a,b in edges:
            # undirected graph
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        res = 0
        for i in range(n):
            if i in visited:
                continue
            
            res += 1
            self.bfs(graph, i, visited)
            
        return res
    
    def bfs(self, graph, node, visited):
        queue = collections.deque([node])
        visited.add(node)
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)        

                    
                    
# DFS
# time: O(V + E), space: O(V)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        res = 0
        for i in range(n):
            if i in visited:
                continue
            
            res += 1
            self.dfs(graph, i, visited)
            
        return res
    
    def dfs(self, graph, node, visited):
        if node in visited:
            return
        
        visited.add(node)
        for neighbor in graph[node]:
            self.dfs(graph, neighbor, visited)
                    
