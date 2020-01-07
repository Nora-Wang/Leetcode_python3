Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.

Example

Example 1:

Input:
push(1)
pop()
push(2)
isEmpty() // return false
top() // return 2
pop()
isEmpty() // return true
Example 2:

Input:
isEmpty()


其实一个queue能很简单的得出stack,但两个queue就需要对queue和stack的特性有很强的理解


code:
class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()
        
    def push(self, x):
        #explain: 对于1234来说,若它每次先push进一个queue,再直接pop+push进另一个queue,这样的结果还是1234,达不到stack的效果
        #但如果是在每次push的时候先当前点加入另一个queue,然后再对之前的结果进行pop+push的操作,这样得到的结果则为4321,即为stack的顺序
        #eg:将1放入queue1,再将queue1赋值给queue2,此时queue1 = None, queue2 = 1
        #将2放入queue1,此时queue1 = 2,再将queue2 = 1用pop+push的方式加入queue1,再将queue1赋值给queue2,此时queue1 = None, queue2 = 2,1
        #将3放入queue1,此时queue1 = 3,再将queue2 = 2,1用pop+push的方式加入queue1,再将queue1赋值给queue2,此时queue1 = None, queue2 = 3,2,1
        self.queue1.append(x)
        while self.queue2:
            self.queue1.append(self.queue2.popleft())
        每次循环结束时,queue2直接被pop完,即queue2 = None,而queue1则是按照先进的排在后面的原则生成的,因此其结果为4321
        self.queue1, self.queue2 = self.queue2, self.queue1

    """
    @return: nothing
    """
    def pop(self):
        self.queue2.popleft()

    """
    @return: An integer
    """
    def top(self):
        return self.queue2[0]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return not self.queue2
