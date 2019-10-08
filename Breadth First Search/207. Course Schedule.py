题目：
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
             
############################################################
topological sort：判读一个有向图，是无环的
############################################################

解题思路：
这就是一个问图能否topological sort的问题，但是因为所给信息的形式是node + edges的形式，因此我们还需要先将其转换为graph字典

数据类型设计：graph{'node':'neighbor'}, indegrees{'node':'indegree_count'}；其中neighbor的数据类型为set，indegree_count为int
########这里要注意理解，后续的indegrees的设计是当发现node有一个neighbor时，它的入度+1
????????

step1:创建graph
step2:计算每个node的indegree数量
step3:用bfs得到满足无环的node，然后与graph中的node个数做比较，若相等，则说明满足topological sort的条件(无环)

code:
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """    
        #step 1: create a graph
        graph = self.create_graph(numCourses, prerequisites)
        
        #step 2: count indegrees of every node
        indegrees = self.count_indegree(graph)
        
        #step 3: use bfs
        #将indegree为0的node放入queue中（即起始node）
        start_nodes = []
        for node in graph:
            if indegrees[node] == 0:
                start_nodes.append(node)
        queue = collections.deque(start_nodes)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            #将node pop出后，其对应的neighbor的indegree直接-1，若该neighbor的indegree此时为0，则其应为此时的起始node，因此需将其加入queue
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        #若无环，则所有的node都应该在result里
        if len(result) == numCourses:
            return True
        else:
            return False
        
######字典的创建：1.设置key 2.设置每个key对应的value

    def create_graph(self, numCourses, prerequisites):
        graph = {}
        for node in range(numCourses):
            graph[node] = set()
        for edge in prerequisites:
        #参考题目中数据的设计[[0,1]]=take course 0 you have to first take course 1
            sub_course, course = edge[0], edge[1]
            graph[sub_course].add(course)
        return graph

    def count_indegree(self, graph):
        indegrees = {}
        for node in graph:
            indegrees[node] = 0
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        return indegrees
        
    
                
        
            
