Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


题目的意思：
1.serialize
将root转化为一个字符串，其中若root.left或root.right为空时记录为‘null,’
注意其最后的输出格式"[1,2,3,null,null,4,5]"

2.deserialize
将一个字符串转化为一个以root为首的树

****************************************************************************************
与449的区别是，449是BST，可以用pre/post order + inorder的方法解决，但297只能用BFS的方法解决
****************************************************************************************


code:
leetcode version
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #因为题中给的serialize的结果为"[1,2,3,null,null,4,5]"，是一个字符串，因此root为空时，直接返回'{}'
        #注意这里的结果要与deserialize的特判相对应
        if not root:
            return '{}'
        
!!#不能直接设置为string，空间占用太多，每次加的时候都相当于重新创建一个新string
#用list，后续直接使用.join()转换
        ser_result = []
        #ser_result = ''
        
        #deque要求参数为list
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
         #注意这里的思路：当这个node存在时，将值加入ser_result,并直接将左右子树加进去。因为当循环到左右子树为node时，若不存在，则会执行else语句
         #不要单独判断node.left和node.right，会出bug
            if node:
                #node.val是int型数据，而结果要求string，因此要用str()
                ser_result.append(str(node.val))
                #ser_result += (str(node.val) + ',')
                queue.append(node.left)
                queue.append(node.right)
            else:
                ser_result.append('null')
                #ser_result += 'null,'
                
        #ser_result = '[' + ser_result + ']'
        #','.join():将list转换为string，每个元素间隔为','
        ser_result = ','.join(ser_result)
        #为了match结果，需要加‘[]’
        ser_result = '[' + ser_result + ']'
        
        return ser_result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #特判None和'{}'
        if not data or data == '{}':
            return None
        
        #split(','):以','为准分割字符串为列表
        #注意这里是data[1:-1]:因为split只会去掉',',而data"[1,2,3,null,null,4,5]"还包括一头一尾的[]，从1开始取，左闭右开，可避免[]
        list_data = data[1:-1].split(',')
        
        #将data中第一个值，即树的root以TreeNode类型的格式加入root
        #list_data[0]是int型
        root = TreeNode(list_data[0])
        
        #deque要求参数为list，所以要加[]
        queue = collections.deque([root])
        index = 1
        
        #个人认为这两个while的逻辑都是一样的，一个是将所有的点都append进queue，当queue为空时，遍历结束
        #一个是直接将index与list_data的长度做比较，当index所指的node超过list_data范围，则意味着所有node都遍历结束
        #但事实上，如果最后剩余的只有#，是不会被append进queue的，而index还没到最大值，还会进入while循环，可这个时候queue为空，所有无法pop
        #while index < len(list_data):
        while queue:
            node = queue.popleft()
            #因为二叉树的特性，除了第一个值，其后面跟的两个值一定是它的left和right
            if list_data[index] != 'null':
                #注意要以TreeNode的格式赋值
                node.left = TreeNode(list_data[index])
                queue.append(node.left)
            index += 1
            
            if list_data[index] != 'null':
                node.right = TreeNode(list_data[index])
                queue.append(node.right)
            index += 1
        
        return root
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))




lintcode version
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return '{}'
            
        ser_result = []
        #ser_result = ''
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                ser_result.append(str(node.val))
                #ser_result += (str(node.val) + ',')
                queue.append(node.left)
                queue.append(node.right)
            else:
                ser_result.append('#')
                #ser_result += '#,'
                
        #将list转换为string，每个元素间隔为','        
        ser_result = ','.join(ser_result)
        ser_result = '{' + ser_result + '}'
        #ser_result = '{' + ser_result + '}'
        
        return ser_result

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if not data or data == '{}':
            return None
        
        ser_list = data[1:-1].split(',')
        index = 0
        deser_result = TreeNode(ser_list[index])
        queue = collections.deque([deser_result])
        index += 1
        
        while queue:
            node = queue.popleft()
            if ser_list[index] != '#':
                node.left = TreeNode(ser_list[index])
                queue.append(node.left)
            index += 1
            
            if ser_list[index] != '#':
                node.right = TreeNode(ser_list[index])
                queue.append(node.right)
            index += 1
        return deser_result
        
