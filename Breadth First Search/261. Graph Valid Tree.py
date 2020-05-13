Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.


code:
#DFS Version
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = self.create(n, edges)
        #graph[node] = [neighbor nodes]
        visited = set()
        
        return self.dfs(0, -1, visited, graph) and len(visited) == n
        
    def dfs(self, node, parent, visited, graph):
        if node in visited:
            return False
        
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue

            if neighbor in visited:
                return False

            res = self.dfs(neighbor, node, visited, graph)
            if not res:
                return False
        
        return True
    
    def create(self, n, edges):
        graph = {}
        
        graph = collections.defaultdict(list)
            
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        return graph
    
    
    
#BFS Version
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = self.create(n, edges)
        #graph[node] = [neighbor nodes]
        queue = collections.deque([0])
        
        visited = set([0])
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                
                queue.append(neighbor)
                visited.add(neighbor)
        
        return len(visited) == n
    
    def create(self, n, edges):
        graph = {}
        
        graph = collections.defaultdict(list)
            
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        return graph
