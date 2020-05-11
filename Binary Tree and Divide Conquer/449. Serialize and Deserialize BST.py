Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


code:
#BFS Version
'''
use BFS to serialize, use space to saperate every level, use # to represent Null node
when deserialize, use split to saparete every level, queue to process every node
time: O(2^depth), space: O(2^depth), completed binary tree 

'''
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            node = queue.popleft()
            
            #deal with null case
            if not node:
                res.append('#,')
                continue
                
            res.append(str(node.val) + ',')
            
            queue.append(node.left)
            queue.append(node.right)
    
        return ''.join(res)
            
            

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        nodes = data.split(',')
        
        #initial root
        root = TreeNode(int(nodes[0]))
        
        queue = collections.deque([root])
        index = 1
        
        while queue:
            node = queue.popleft()
            
            #deal with left child
            if nodes[index] == '#':
                node.left = None
            else:
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            
            #deal with right child
            if nodes[index] == '#':
                node.right = None
            else:
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
            
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



#pre-order + in-order Version
'''
serialize: use preorder traverse get string
deserialize: split by space, get preorder list, use sort to get inorder result, utilize pre-order + in-order to construct the BST (leetcode 105)
time: O(n^2), space: O(n)
'''
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        
        res = []
        stack = []
        
        while root or stack:
            if root: 
                stack.append(root)
                res.append(str(root.val))
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        
        return ' '.join(res)
        
        
        
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        preorder = data.split()
        for i in range(len(preorder)):
            preorder[i] = int(preorder[i])
            
        inorder = sorted(preorder)
        
        return self.helper(preorder, inorder)
        
    def helper(self, preorder, inorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        
        root.left = self.helper(preorder[1:index + 1], inorder[:index])
        root.right = self.helper(preorder[index + 1:], inorder[index + 1:])
        
        return root
