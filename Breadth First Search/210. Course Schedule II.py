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
#两个corner case！！



code:
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #corner case 1
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        graph, indegrees = self.create_graph_indegrees(numCourses, prerequisites)
        
        queue = collections.deque()
        for course in indegrees:
            if indegrees[course] == 0:
                queue.append(course)
        
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            
            for next_course in graph[course]:
                indegrees[next_course] -= 1
                
                if indegrees[next_course] == 0:
                    queue.append(next_course)
        
        #corner case 2
        return res if len(res) == numCourses else []
        
        
    def create_graph_indegrees(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        indegrees = {i:0 for i in range(numCourses)}
        
        for curt, prev in prerequisites:
            indegrees[curt] += 1
            graph[prev].append(curt)
            
        return graph, indegrees
        
        
