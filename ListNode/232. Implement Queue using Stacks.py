Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).


#注意判断empty的条件是in和out都为空
#stack是先进后出,即它的front在后面 eg:[1,2,3] front是3
code:
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.out_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            
        return self.out_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.in_stack) == 0 and len(self.out_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
