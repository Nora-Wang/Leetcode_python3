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
这道题其实就是求是否有唯一的topological sort的结果。（3 steps: create graph, count indegrees, topological）
topological sort的实质是将所有的node按其本身的顺序从头到尾的遍历一遍（遍历一个无环的有向图）

什么情况下会有不止一种结果呢？就是当某一时刻有不止一个indegree为0的node的时候。所以我们只需要监测len(queue) > 1即可
也就是整个遍历完所有的node，只有一个结果，即一条有向线；因此每一层的indegree为0的node只有一个，即每层queue只有一个


具体做法：
用seqs生成一个graph，计算indegrees，然后进行拓扑排序，其得到的遍历结果唯一，且等于org

code：
一共3个版本，因为lintcode和leetcode判定条件不同，第三个版本两个都能用，为最佳

#leetcode版本
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


    
#lintcode版本
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        
        #step 1: create a graph
        graph = self.create_graph(seqs)
        #step 2: count indegrees
        indegrees = self.count_indegrees(graph)
        #step 3: topological
        topo_record = self.bfs_topological(graph, indegrees)
        return org == topo_record

    def create_graph(self, seqs):
        graph = {}
        for edge in seqs:
            for node in edge:
                if node not in graph:
                    graph[node] = set()
        for edge in seqs:
            for i in range(len(edge) - 1):
                node = edge[i]
                neighbor = edge[i + 1]
                graph[node].add(neighbor)
        return graph
    
    def count_indegrees(self, graph):
        indegrees = {}
        for node in graph:
            indegrees[node] = 0
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        return indegrees
          
    def bfs_topological(self, graph, indegrees):
        #step 3: topological sorting
        queue = collections.deque([])
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
        topo_record = []
        while queue:
            #一定不止一个拓扑排序结果
            if len(queue) > 1:
                return False
            node = queue.popleft()
            topo_record.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return topo_record

    
    
#lintcode和leetcode通用版本
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        #step 1: create a graph
        graph = self.create_graph(org, seqs)
        #为符合leetcode的特判：当graph生成为None(seqs中的node与org不同)，且此时org不为None时，返回False
        #org:[1]
        #seqs:[[1],[2,3],[3,2]]
        if not graph and org:
            return False
        
        #step 2: count indegrees
        indegrees = self.count_indegrees(graph)
        
        #step 3: topological
        topo_record = self.bfs_topological(graph, indegrees)
        #将拓扑排序的结果与org比较
        return org == topo_record
    
###g整个graph的生成其实只用到了seqs，由此避免了corner case，比如输入[[]], [[1]]
    def create_graph(self, org, seqs):
        graph = {}
        #记录seqs出现的node(leetcode corner case:[1,2,3], [[1,2],[1,3],[2,3][4,5]]
        record = set()
        for edge in seqs:
            for node in edge:
                if node not in graph:
                    graph[node] = set()
                    record.add(node)
        for edge in seqs:
            #注意i的取值范围，因为后续会用到i+1
            for i in range(len(edge) - 1):
                node = edge[i]
                neighbor = edge[i + 1]
                graph[node].add(neighbor)
        if len(record) != len(org):
            return None
        return graph
    
    def count_indegrees(self, graph):
        indegrees = {}
        for node in graph:
            indegrees[node] = 0
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        return indegrees
        
    
    def bfs_topological(self, graph, indegrees):
        queue = collections.deque([])
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
        #记录拓扑排序结果
        topo_record = []
        while queue:
            #一定不止一个拓扑排序结果
            if len(queue) > 1:
                return False
            node = queue.popleft()
            topo_record.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return topo_record
            
