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
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque

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
#这里是将node给copy进mapping这个字典里，mapping的key是每个node的值，value是Node类型的node(即包括val和neighbors)
#之所以是mapping字典，可参考程序结果的数据结构
        mapping = {}
#这里的copy若直接用mapping[node.val] = node,当node被改变时，mapping里的node也会改变
#因此这里使用mapping[node.val] = Node(node.val, [])，相当于重新创建一个class为Node的变量，使它的.val值=node.val
        for node in nodes:
            mapping[node.val] = Node(node.val, [])
            
        #step3: copy edges(neighbors)
        for node in nodes:
#这里需要设置一个new_node是为了便于后续对mapping中的node加入neighbors。这里注意，neighbors也得是Node类型
#mapping字典，它的键是node.val，value是new_node
#new_node包含new_node.val和new_node.neighbors
#即翻译一下：new_node.neighbors = mapping[node.val].neighbors
#因此将new_neighbor加入new_node就直接能改变mapping
            new_node = mapping[node.val]
            for neighbor in node.neighbors:
#！！！这里注意，neighbors也得是Node类型；就类似于左子树和右子树，得以树的形式与root相连
                new_neighbor = mapping[neighbor.val]
                new_node.neighbors.append(new_neighbor)
        
        return mapping[root.val]
    
    
#思路：先把node放入result，然后判断其neighbor，若neighbor不在结果中，则加入queue，后续可pop出加入result
#（这里之所以需要加入queue，而不是直接加入result，是因为neighbor可能还有neighbor，直接加入则无法判断）
    def getNodes(self, node):
#？？？为什么要用set：set的话判断一个node在不在set里，可以直接找到有没有这个node
        result = set([])
        queue = deque([node])
        while queue:
            node = queue.popleft()
            result.add(node)
            for neighbor in node.neighbors:
                if neighbor not in result:
                    queue.append(neighbor)
        return result
