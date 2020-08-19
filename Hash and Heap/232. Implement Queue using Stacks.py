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


# 因为queue是FIFO，而stack是FILO，因此在用stack表示queue的时候需要用两个stack
# 第二个helper_stack主要用于queue的pop和找peek，因为queue在pop/找peek时应该是整个地址的bottom
# 过程：先把stack一个一个的pop出，存入helper_stack，以得到queue的bottom；然后将helper_stack的内容重新放入stack中

'''
when we should use two stacks to implement a queue?
The application for this implementation is to separate read & write of a queue in multi-processing. One of the stack is for read, and another is for write. 
They only interfere each other when the former one is full or latter is empty.
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.helper_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move_out()
        res = self.stack.pop()
        self.move_back()
        
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.move_out()
        peek = self.stack.pop()
        self.stack.append(peek)
        self.move_back()
        
        return peek

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0
    
    def move_out(self) -> None:
        while len(self.stack) > 1:
            self.helper_stack.append(self.stack.pop())
    
    def move_back(self) -> None:
        while self.helper_stack:
            self.stack.append(self.helper_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
