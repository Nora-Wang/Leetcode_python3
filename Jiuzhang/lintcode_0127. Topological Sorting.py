Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

Example
For graph as follow:

图片

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
Challenge
Can you do it in both BFS and DFS?

Clarification
Learn more about representation of graphs

Notice
You can assume that there is at least one topological order in the graph.


topological sorting
在图论中，由一个有向无环图的顶点组成的序列，当且仅当满足下列条件时，称为该图的一个拓扑排序（英语：Topological sorting）。
1.每个顶点出现且只出现一次；
2.若A在序列中排在B的前面，则在图中不存在从B到A的路径。
也可以定义为：拓扑排序是对有向无环图的顶点的一种排序，它使得如果存在一条从顶点A到顶点B的路径，那么在排序中B出现在A的后面。


graph是现成的，所以只用count indegrees，然后bfs就行
注意：
1.这里的graph不是一个dirc，而是一个DirectedGraphNode类，所以在调用neighbors的时候不一样
2.indegrees被设计为dirc，因为题目没说node是从1到n的，所以不好用list来设计indegrees
3.题目中的Notice有说，至少有一个拓扑排序的结果，所以不需要len(result) == len(indegrees)，以判断是否满足所有点都遍历过（即拓扑排序的条件）



code:
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        #step 1: count indegrees
        indegrees = self.count_indegrees(graph)
        
        #step 2: bfs
        result = []
        queue = collections.deque()
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
        while queue:
            node = queue.popleft()
            result.append(node)
            #注意是node.neighbors
            for neighbor in node.neighbors:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return result
        
    def count_indegrees(self, graph):
    #indegrees的数据类型为dirc
        indegrees = {}
        for node in graph:
            indegrees[node] = 0
        for node in graph:
            for neighbor in node.neighbors:
                indegrees[neighbor] += 1
        return indegrees
