Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.



# 12/09/2020
# utilize inorder iterator traverse: everytime go to the most left node, use stack to record path, as stack_last_node.right as new root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []

    def next(self) -> int:
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        
        next_node = self.stack.pop()
        self.root = next_node.right
        return next_node.val

    def hasNext(self) -> bool:
        # or self.root: avoid do hasNext before next function
        return len(self.stack) or self.root


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()











#05/02/2020
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
brute force
use a stack to record the result of inorder traverse
time: O(n)(for the inital, but for the next/hasnext function, the time should be O(1)), space: O(n)

optimize
utinize inorder iterate thoughts
use a stack to record the left path, when need to get next node, pop it from the stack directly.
point: after pop a node from stack, go to the node.right, record the left path of the node.right subtree

time: average O(1)???, space: O(h)
'''


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        min_node = self.stack.pop()
        res = min_node.val
        
        #renew the stack
        node = min_node.right
        while node:
            self.stack.append(node)
            node = node.left
        
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()










思路：
      5
    /  \
  3      7 
 / \    / 
2   4  6

1.def __init__(self, root)将5，3，2放入stack
2.def next(self)
先将2pop出，然后将3pop出，因为2是3的left，因此需要判断3是否存在right，存在则将4放入stack，由于4没有左右子树，因此直接pop即可
将5pop出，由于3是5的left，因此需要判断5的right，此时存在right=7，将7也加入stack，此时又要将7的左下节点(6)全部放入stack
将6pop出，继续将7pop出，由于6是7的left，但7没有right
#即当前节点为下一个节点的left时，先pop出下一个节点，然后需要对下一个节点的right进行判断，若存在，则需要无限向左下append；若不存在则继续pop
将6pop出，继续将7pop出，由于6是7的left，但7没有right
3.def hasNext(self)此时所有节点都被遍历过，stack为空

code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
     #将从root开始一直到最左边的node全都放入stack中
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        #最左的node
        node = self.stack[-1]
       
        #若最左的node有right节点，则将node.right的一路向左的节点也都放入stack
        if node.right:
            n = node.right
            while n:
                self.stack.append(n)
                n = n.left
              
        #当没有右节点时，向外pop，直至current被pop出的node是下一个将要被pop出的node的left时，停止
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
            
        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        #当stack里还有node，则说明还有next
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
