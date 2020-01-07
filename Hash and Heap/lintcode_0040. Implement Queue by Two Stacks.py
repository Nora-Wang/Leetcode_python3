As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

Example

Example 1:

Input:
    push(1)
    pop()    
    push(2)
    push(3)
    top()    
    pop()     
Output:
    1
    2
    2
Example 2:

Input:
    push(1)
    push(2)
    push(2)
    push(3)
    push(4)
    push(5)
    push(6)
    push(7)
    push(1)
Output:
[]
Challenge

implement it by two stacks, do not use any other data structure and push, pop and top should be O(1) by AVERAGE.

Notice

Suppose the queue is not empty when the pop() function is called.


用两个stack来表示queue
self.stack2里的内容等同于queue pop时的顺序

code:
class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        self.stack1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        self.top()
        return self.stack2.pop()

    """
    @return: An integer
    """
    def top(self):
###这里一定要先判断self.stack2是否为空
#eg:1.self.stack1 = 123,从而生成self.stack2 = 321
#2.当self.stack1新加入456后,若self.stack2不为空,直接将self.stack1加入self.stack2的结果为self.stack2 = 321654,
#但事实上应该先pop123,然后才456
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
