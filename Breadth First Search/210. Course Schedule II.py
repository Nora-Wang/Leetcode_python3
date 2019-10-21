题目：
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
             
             
             
主题思路跟207一模一样，只是I用count记录node个数，若与numCourses相同即符合
而II则需要用result记录所遍历的courses，若其长度与numCourses相同即符合，然后输出result

code:
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        #step 1
        graph, indegrees = self.create_graph_indegrees(numCourses, prerequisites)
        
        queue = collections.deque([])
        #step 2
        #此处可用range(numCourses)，也可用graph
        for node in range(numCourses):
            if indegrees[node] == 0:
                queue.append(node)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        if len(result) == numCourses:
            return result
        else:
            return []
        
    def create_graph_indegrees(self, numCourses, prerequisites):
        graph = {}
        indegrees = []
        for course in range(numCourses):
            graph[course] = set()
            indegrees.append(0)
        for edge in prerequisites:
            sub_course = edge[0]
            course = edge[1]
       #####注意点！！避免重复计算indegrees
            if sub_course not in graph[course]:
                graph[course].add(sub_course)
                indegrees[sub_course] += 1
        return graph, indegrees






Boss版本
此版本有个注意点：在graph的创建上跟207一样，但这道题需要result.reverse()，因为Boss的逻辑是反的，所以结果也是反的
code:
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = self.create_graph(numCourses, prerequisites)
        
        indegrees = self.count_indegrees(graph)
        
        start_nodes = []
        for node in graph:
            if indegrees[node] == 0:
                start_nodes.append(node)
        queue = collections.deque(start_nodes)
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(result) == numCourses:
            result.reverse()
            return result
        else:
            return None
        
    
    def create_graph(self, node, neighbor):
        graph = {}
        for n in range(node):
            graph[n] = set()
        for edge in neighbor:
            sub_node, node = edge[0], edge[1]
            graph[sub_node].add(node)
        return graph
    
    def count_indegrees(self, graph):
        indegrees = {}
        for node in graph:
            indegrees[node] = 0
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        return indegrees
