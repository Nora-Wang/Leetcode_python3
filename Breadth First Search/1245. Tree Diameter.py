Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

 

Example 1:



Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: 
A longest path of the tree is the path 1 - 0 - 2.
Example 2:



Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: 
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 

Constraints:

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.




# time: O(n), space: O(n)
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not len(edges) or not len(edges[0]):
            return 0
        
        # {node:neighbors}
        graph = collections.defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        last_node, _ = self.bfs(edges[0][0], graph)
        _, longest = self.bfs(last_node, graph)
        
        return longest
    
    def bfs(self, node, graph):
        queue = collections.deque([node])
        distance = 0
        visited = set([node])
        last_node = node
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        last_node = neighbor
            
            distance += 1
        
        return last_node, distance - 1
