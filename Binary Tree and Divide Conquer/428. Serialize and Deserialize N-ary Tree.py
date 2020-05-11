"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
'''
similar with 297, but the most difficult part is how to design the serialized result

serialize:
use the second example in the topic: saperate every node and its children with null.
case 1: if there only has one null, which means process continue to next new node
case 2: if there has two consequence null, which means process continue to next new node and this node's children is []

deserialize:
the most difficult part: how to deal with the two cases of 'null'
method: both of the two cases just need to continue to pop the next new node. 
case 1: just continue pop
case 2: firstly continue pop, move to the new one, seconde pop make curt node's children be defaulted, which is [], 
move to a next new node 

edge case: queue maybe empty

time: O(n), space: O(n)

'''
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            node = queue.popleft()
            
            if node == 'null':
                res.append('null')
                continue
            
            res.append(str(node.val))
            queue.append('null')
            
            for child in node.children:
                queue.append(child)
                    
        return ' '.join(res)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        data = data.split()
        root = Node(int(data[0]), [])
        queue = collections.deque([root])
        index = 1
        
        #[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
        #end case is when all the node in data have been dealed with
        while index < len(data):
            #sometimes the queue maybe empty, because last node haven't been dealed with(eg: 1)
            if queue:
                node = queue.popleft()
            
            while data[index] != 'null':
                child = Node(int(data[index]), [])
                node.children.append(child)
                queue.append(child)
                index += 1
            
            index += 1
            
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
