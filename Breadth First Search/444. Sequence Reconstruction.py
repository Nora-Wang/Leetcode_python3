code:
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true


思路：
这道题其实就是求是否有唯一的topological sort的结果。（3 steps）
什么情况下会有不止一种结果呢？就是当某一时刻有不止一个indegree为0的node的时候。所以我们只需要监测queue.size() > 1即可
也就是整个遍历完只有一个结果，即一条线；因此每一层的indegree为0的node只有一个，即每层queue只有一个


code:
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        #step 1: create graph
        graph = self.create_graph(org, seqs)
        if graph is None:
            return False
        
        
        #step 2: count indegree for every node
        indegrees = self.count_indegrees(graph)
        
        
        #step 3: bfs, topological sorting
        queue = collections.deque()
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
        while queue:
        ###因为只有唯一topological sort的结果，也就是整个遍历完只有一个结果，即一条线；因此每一层的indegree为0的node只有一个，即每层queue只有一个
            if len(queue) > 1:
                return False
            
            node = queue.popleft()
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        ###特殊情况org = [1], seqs = [[1],[1]]
        #node 1的indegree=1，其neighbor为node 1，因为没有indegree为0的node，因此不进入queue
        for node in graph:
            if indegrees[node] != 0:
                return False
        return True
    
    def create_graph(self, org, seqs):
        graph = {}
        #判断seqs的取值是否在org内
        count = set()
        
        for node in org:
            graph[node] = set()
        for edge in seqs:
            #record the nodes in seqs
            for node in edge:
                count.add(node)
                
            for i in range(0, len(edge) - 1):
                node = edge[i]
                sub_node = edge[i + 1]
                #特殊情况org: [1,2,3], seqs: [[-1,1000]];即限制seqs的取值一定要在(1, len(org))之间
                if min(node, sub_node) < 1 or max(node, sub_node) > len(org):
                    return None
                    
                graph[node].add(sub_node)
                
        #org: [1,2,3], seqs: [[1,2]]
        if len(count) != len(org):
            return None
        return graph
    
    def count_indegrees(self, graph):
        indegrees = {}
        for node in graph:
            indegrees[node] = 0
        for node in graph:
            for sub_node in graph[node]:
            ###注意这里是sub_node。理解indegrees的意义
                indegrees[sub_node] += 1
        return indegrees
