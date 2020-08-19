Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).


# 具体可参考232，类似


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.helper_queue = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.move_out()
        res = self.queue.popleft()
        self.move_back()
        
        return res

    def top(self) -> int:
        """
        Get the top element.
        """
        self.move_out()
        stack_top = self.queue.popleft()
        self.move_back()
        
        # 注意这里一定要最后才加入queue，因为stack_top是queue的top，即queue[-1]
        self.queue.append(stack_top)
        return stack_top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0
    
    def move_out(self) -> None:
        while len(self.queue) > 1:
            self.helper_queue.append(self.queue.popleft())
            
    def move_back(self) -> None:
        while self.helper_queue:
            self.queue.append(self.helper_queue.popleft())


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
