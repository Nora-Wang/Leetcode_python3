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
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.


#BFS Version
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = self.create(n, edges)
        
        count = 0
        visited = set()
        for node in range(n):
            if node in visited:
                continue
            visited.add(node)
            count += 1
            self.bfs(graph, visited, node)
    
        return count
    
    def create(self, n, edges):
        graph = {}
        
        for node in range(n):
            graph[node] = []
            
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        return graph
    
    def bfs(self, graph, visited, node):
        queue = collections.deque([node])
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                
                visited.add(neighbor)
                queue.append(neighbor)

#DFS Version
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = self.create(n, edges)
        
        count = 0
        visited = set()
        for node in range(n):
            if node in visited:
                continue
            count += 1
            self.dfs(graph, visited, node)
    
        return count
    
    def create(self, n, edges):
        graph = {}
        
        graph = collections.defaultdict(list)
            
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        return graph
    
    def dfs(self, graph, visited, node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            self.dfs(graph, visited, neighbor)

#典型Union Find的题目
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #corner case
        if not edges:
            return n
        
        #初始化父集,使所有的点的父亲都指向自己
        self.point_to_father = {}
        for i in range(n):
            self.point_to_father[i] = i
            
        #对于存在边的每个点做并查集
        for edge in edges:
            self.union(edge[0], edge[1])
        
        #找到作为根的节点的个数,就是连通图的个数
        count = 0
        for point in self.point_to_father:
            if self.point_to_father[point] == point:
                count += 1
                
        return count
    
    #Union set
    #当发现相连的两个点的根结点不同时,将其中一个直接化为另一个的子树
    def union(self, point_a, point_b):
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        
        if root_a != root_b:
            self.point_to_father[root_a] = root_b
    
    #Find set + Compressed path
    #记录当前点走到根结点的路径,然后将所经过的所有点的根节点都记录为最终根节点
    def find(self, point):
        path = []
        
        while self.point_to_father[point] != point:
            path.append(point)
            point = self.point_to_father[point]
        
        for p in path:
            self.point_to_father[p] = point
        
        return point
