For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

code:
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2 or not edges:
            return [i for i in range(n)]
        
        graph, indegrees = self.create_graph(n, edges)
        #graph[node] = [sub_nodes]
        #indegrees[node] = how many pre_nodes
        
        #because undirected graph, the minmum indegrees should be 1
        queue = collections.deque([])
        for node in range(n):
            if indegrees[node] == 1:
                queue.append(node)
        
        #the result should be the last level of the topological nodes, which means the mid-nodes of the graph
        #because the mid-nodes' height = length of the graph // 2, others nodes' height must larger than mid-nodes
        res = []
        
        while queue:
            res = list(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                for sub_node in graph[node]:
                    indegrees[sub_node] -= 1
                    
                    if indegrees[sub_node] == 1:
                        queue.append(sub_node)
        
        return res
    
    def create_graph(self, n, edges):
        graph = {}
        indegrees = {}
        
        for i in range(n):
            graph[i] = []
            indegrees[i] = 0
            
        for node, sub_node in edges:
            graph[node].append(sub_node)
            graph[sub_node].append(node)
            
            indegrees[node] += 1
            indegrees[sub_node] += 1
        
        return graph, indegrees
                
    
