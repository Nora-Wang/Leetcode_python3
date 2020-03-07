Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:

-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.


code:
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        if not self.max_stack:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(x, self.max_stack[-1]))

    def pop(self) -> int:
        self.max_stack.pop()
        
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def peekMax(self) -> int:
        return self.max_stack[-1] if self.max_stack else None

    def popMax(self) -> int:
        Max = self.max_stack[-1]
        
        temp = []
        while self.stack and self.stack[-1] != Max:
            temp.append(self.stack.pop())
            self.max_stack.pop()
            
        self.stack.pop()
        self.max_stack.pop()
        
        
        for num in temp[::-1]:
            self.push(num)
        
        return Max


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
