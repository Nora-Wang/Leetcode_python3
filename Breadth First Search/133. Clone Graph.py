题目：
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

 

Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.


思路：分为3步
1.找到所有的node
2.用完全copy的办法copy所有的node
3.copy edges




code:
leetcode版本
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
      
        root = node
        
        #step1: find all the nodes
        nodes = self.getNodes(node)
        
        #step2: copy nodes
#这里是将node给copy进mapping这个字典里，mapping的key是每个老node，value是新创建的Node类型的clone_node(即包括val和neighbors)
#这里的copy若直接用mapping[node] = node,当node被改变时，mapping里的node也会改变
#因此这里使用mapping[node] = Node(node.val, [])，相当于重新创建一个class为Node的变量，使它的.val值=node.val,.neighbors为[]
        mapping = {}
        for node in nodes:
#注意，此处指copy了node.val，对于新node，其node.neighbors是空的，因此需要step3
#注意此处用mapping[node]而不是node.val是因为可能存在一种情况：node.val相等但node.neighbors不等，这时的node是不同的
            #mapping[node.val] = Node(node.val, [])
            mapping[node] = Node(node.val, [])

            
        #step3: copy edges(neighbors)
        for node in nodes:
#对于mapping字典，它的key是node，value是clone_node,他们都是Node型数据
#clone_node包含clone_node.val和clone_node.neighbors
            for neighbor in node.neighbors:
#！！！这里注意，加入neighbors的clone_neighbor也得是Node类型；就类似于左子树和右子树，得以树的形式与root相连
#mapping[node].neighbors.append(mapping[neighbor.val])不行，参考前面的mapping[node.val]
                mapping[node].neighbors.append(mapping[neighbor])
 
#此处要用root，是因为代码命名时多次用到node，此时的node不再是程序原本给的参数node了，因此在前面需要先将node赋值给root
        return mapping[root]
    
    
#思路：先把node放入result，然后判断其neighbor，若neighbor不在结果中，则加入queue，后续可pop出加入result
#这里之所以需要加入queue，而不是直接加入result，是因为neighbor可能还有neighbor，直接加入则无法判断

    def getNodes(self, node):
#为什么要用set：判断一个node在不在set里，可以直接找到有没有这个node；而list则需要一个一个的查找
        #不能写成result = set(),这样在同一层的时候，会重复访问node，找其neighbors
        #result = set()
        #reslut记录已进入过queue的nodes
        result = set([node])
    
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
        
            #reslut.add(node)
            #不能这样写，而应该在后续使用result.add(neighbor)
            #原因是这样写与后续的定义不同
            #reslut.add(node)的意思是已经进入队列，然后从里面pop出的nodes有哪些
            #而result.add(neighbor)的意思是能够进入队列的nodes有哪些
            #reslut.add(node)会造成同时属于不同root的node会重复进入队列
            #eg：A.right = B.left = C, A与B属于同一层
            #当在pop A、B时，会将其子树都遍历一遍，这样C将会被重复append进队列
            
            for neighbor in node.neighbors:
        #这里一定要加if语句，虽然实质上是没差距的(因为set不会存储重复数据),但是加一句可以节省时间复杂度，否则容易Time Limit Exceeded
                if neighbor not in result:
                    queue.append(neighbor)
                    result.add(neighbor)
        return result


       
lintcode版本
两者的不同：Node类型定义的不同
具体代码含义，可参照leetcode注释
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if not node:
            return None
        root = node
        #step 1: find nodes
        nodes = self.find_nodes(node)
        
        #step 2: copy nodes
        graph = {}
        for node in nodes:
            graph[node] = UndirectedGraphNode(node.label)
            
        #此时的graph：key为node，value为new_node，node与new_node都是UndirectedGraphNode类型的
        #step 3: copy edges
        for node in nodes:
            for neighbor in node.neighbors:
                graph[node].neighbors.append(graph[neighbor])
        return graph[root]
        
    def find_nodes(self, node):
        #不能写成result = set(),这样在同一层的时候，会重复访问node，找其neighbors
        #result = set()
        #reslut记录已进入过queue的nodes
        result = set([node])
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            
            #reslut.add(node)
            #不能这样写，而应该在后续使用result.add(neighbor)
            #原因是这样写与后续的定义不同
            #reslut.add(node)的意思是已经进入队列，然后从里面pop出的nodes有哪些
            #而result.add(neighbor)的意思是能够进入队列的nodes有哪些
            #reslut.add(node)会造成同时属于不同root的node会重复进入队列
            #eg：A.right = B.left = C, A与B属于同一层
            #当在pop A、B时，会将其子树都遍历一遍，这样C将会被重复append进队列
            for neighbor in node.neighbors:
                if neighbor not in result:
                    queue.append(neighbor)
                    result.add(neighbor)
        return result
        
            
        
            
