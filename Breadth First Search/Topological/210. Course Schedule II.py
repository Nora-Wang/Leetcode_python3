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
             
             
#BFS Version             
主题思路跟207一模一样，只是I用count记录node个数，若与numCourses相同即符合
而II则需要用result记录所遍历的courses，若其长度与numCourses相同即符合，然后输出result
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, neighbors = self.create(numCourses, prerequisites)
        #graph = {pre_course:courses}
        #neighbors = {course:how many pre_courses for this course}
        
        res = []
        
        queue = collections.deque()
        for course in neighbors:
            if neighbors[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            res.append(course)
            for sub_course in graph[course]:
                neighbors[sub_course] -= 1
                
                if neighbors[sub_course] == 0:
                    queue.append(sub_course)
        
        return res if len(res) == numCourses else []
    
    def create(self, numCourses, prerequisites):
        graph, neighbors = collections.defaultdict(list), {}
        
        for course in range(numCourses):
            neighbors[course] = 0
            
        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
            neighbors[course] += 1
        
        return graph, neighbors
        
        
#DFS Version
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
        
        #0  means haven't been visited
        #-1 means have been visited
        #1  means visiting
        visited = [0 for _ in range(numCourses)]
        
        #to record the visited courses
        order = []
        
        for course in range(numCourses):
            if self.dfs(graph, visited, course, order):
                return []
        
        #because we go to the end course and pop it one by one, then add the courses into order, the order of courses are reversed
        return reversed(order)
    
    def dfs(self, graph, visited, course, order):
        #this course is in visiting list -> have circle -> end the recursion
        if visited[course] == 1:
            return True
        #this course has been visited -> don't need to visite it anymore
        if visited[course] == -1:
            return False
        
        #mark this course as visiting
        visited[course] = 1
        for sub_course in graph[course]:
            #if any sub_course for curt course have a circle -> end the recursion
            if self.dfs(graph, visited, sub_course, order):
                return True
        
        #mark this course as has been visited
        visited[course] = -1
        #add this course to order
        order.append(course)
        
        return False
