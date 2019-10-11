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




code:
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #step 1: create graph
        graph = self.create_graph(n, edges)
        
        #step 2: count indegrees
        indegrees = self.count_indegrees(graph)
        
        #step 3: bfs, topological sort
        queue = collections.deque([0])
        result = 0
        visited = set()
        
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    result += 1
                elif indegrees[neighbor] == 1 and neighbor not in visited:
                    queue.append(neighbor)
                    
        return result
    
    
    def create_graph(self, n, edges):
        graph = {}
        for node in range(n):
            graph[node] = set()
        for node in graph:
            for e in edges:
                node = e[0]
                neighbor = e[1]
                graph[node].add(neighbor)
                graph[neighbor].add(node)
        return graph
    
    def count_indegrees(self, graph):
        indegrees = {}
        for node in graph:
            indegrees[node] = 0
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        return indegrees
                
        
