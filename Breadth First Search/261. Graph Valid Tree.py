题目：
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.



思路：
树的两个性质：
1. #node = 1 + #edge
2. 所有node连通 （用bfs能遍历所有的node，看是否connected）；


注意：题目中给的是node个数以及edges，我们需要先把图转换为graph的形式，然后再做bfs
为了应对back edge，我们需要用一个HashSet visited记录已经visited的node，将其与n做比较

另外要注意，所给的边都是directed的，我们需要将图转化为undirected的，即graph[node].add(neighbor) + graph[neighbor].add(node)


code:

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        #性质1判断
        if len(edges) != n - 1:
            return False
            
        #创建graph
        graph = self.create_graph(n, edges)
        
        #bfs
        visited = set()
        queue = collections.deque([0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return n == len(visited)
    
    def create_graph(self, n, edges):
        graph = {}
        for node in range(n):
            graph[node] = set()
        for edge in edges:
            node = edge[0]
            neighbor = edge[1]
    #####注意点，undirected
            graph[node].add(neighbor)
            graph[neighbor].add(node)
        return graph
                
            
