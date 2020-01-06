import collections

class Solution:
    def is_blocked(self, required_tasks, task_from, task_to):
        if not required_tasks or not task_from or not task_to:
            return True

        graph, indegrees = self.create_grpah_indegrees(required_tasks, task_from, task_to)

        queue = collections.deque([])
        for task in required_tasks:
            if indegrees[task] == 0:
                queue.append(task)

        count = 0
        #path = []
        #print(graph)
        #print(indegrees)
        while queue:
            task = queue.popleft()
            count += 1
            #path.append(task)
            for sub_task in graph[task]:
                indegrees[sub_task] -= 1
                if indegrees[sub_task] == 0:
                    queue.append(sub_task)


        #print(path)
        return count != len(required_tasks)


    def create_grpah_indegrees(self, required_tasks, task_from, task_to):
        graph = {}
        indegrees = {}

        for task in required_tasks:
            graph[task] = set()
            indegrees[task] = 0

        for i in range(len(task_from)):
            prev = task_from[i]
            sub = task_to[i]

            if prev in required_tasks and sub in required_tasks:
                graph[prev].add(sub)
                indegrees[sub] += 1

        return graph, indegrees

solution = Solution()

'''required_tasks = ['get gas', 'drive', 'load materials', 'exit']
task_from = ['get gas', 'drive', 'load materials']
task_to = ['drive', 'exit', 'exit']'''


required_tasks = ['get gas', 'drive', 'exit','load materials']
task_from = ['get gas', 'drive', 'load materials','exit']
task_to = ['drive', 'exit', 'exit', 'load materials']

result = solution.is_blocked(required_tasks, task_from, task_to)

print(result)
