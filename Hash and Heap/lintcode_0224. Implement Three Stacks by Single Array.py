Implement three stacks by single array.

You can assume the three stacks has the same size and big enough, you don't need to care about how to extend it if one of the stack is full.

Example

ThreeStacks(5)  // create 3 stacks with size 5 in single array. stack index from 0 to 2
push(0, 10) // push 10 in the 1st stack.
push(0, 11)
push(1, 20) // push 20 in the 2nd stack.
push(1, 21)
pop(0) // return 11
pop(1) // return 21
peek(1) // return 20
push(2, 30)  // push 30 in the 3rd stack.
pop(2) // return 30
isEmpty(2) // return true
isEmpty(0) // return false


重点是如何使用1个array来实现3个stack:使用self.array_stack = [None] * (size * 3),每一个size长度的array代表一个stack

code:
class ThreeStacks:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        self.array_stack = [None] * (size * 3)
        self.stack_point1, self.stack_point2, self.stack_point3 = 0, size, size * 2

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """
    def push(self, stackNum, value):
        if stackNum == 0:
            self.array_stack[self.stack_point1] = value
            self.stack_point1 += 1

        if stackNum == 1:
            self.array_stack[self.stack_point2] = value
            self.stack_point2 += 1
        
        if stackNum == 2:
            self.array_stack[self.stack_point3] = value
            self.stack_point3 += 1
            
        return

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def pop(self, stackNum):
        if stackNum == 0:
            self.stack_point1 -= 1
            pop_result = self.array_stack[self.stack_point1]

        if stackNum == 1:
            self.stack_point2 -= 1
            pop_result = self.array_stack[self.stack_point2]
        
        if stackNum == 2:
            self.stack_point3 -= 1
            pop_result = self.array_stack[self.stack_point3]
        
        return pop_result

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def peek(self, stackNum):
        if stackNum == 0:
            return self.array_stack[self.stack_point1 - 1]
        
        if stackNum == 1:
            return self.array_stack[self.stack_point2 - 1]
        
        if stackNum == 2:
            return self.array_stack[self.stack_point3 - 1]

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """
    def isEmpty(self, stackNum):
        if stackNum == 0:
            return self.stack_point1 == 0
        
        if stackNum == 1:
            return self.stack_point2 == self.size
        
        if stackNum == 2:
            return self.stack_point3 == self.size * 2
        
