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


'''
when we should use two stacks to implement a queue?
The application for this implementation is to separate read & write of a queue in multi-processing. One of the stack is for read, and another is for write. 
They only interfere each other when the former one is full or latter is empty.
'''

# Version 1: 在pop的时候倒
# stack2只是一个辅助作用，实际上所有的值还是以stack的形式被存在stack1里，只有当需要执行pop function时才利用stack2得到结果
# stack1[0] = queue front, stack1[-1] = queue bottom
# 过程：先把stack1一个一个的pop出，存入stack2，以得到queue的front；然后将stack2的内容重新放入stack1中
# time: push O(1), pop O(n)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move_out()
        res = self.stack2.pop()
        self.move_in()
        
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack1[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0
    
    def move_out(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
    
    def move_in(self):
        while self.stack2:
            self.stack1.append(self.stack2.pop())



# Version 2: 在push的时候倒
# 这里是以stack2为标准，stack1作为辅助
# 过程：每次需要push时，要先将stack2的内容一个一个pop出，放入stack1，然后直接在当前stack1中append x，最后再将stack1的内容放入stack2
# stack2[0] = queue bottom, stack2[-1] = queue front
# time: push O(n), pop O(1)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.move_out()
        self.stack1.append(x)
        self.move_in()

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack2) == 0
    
    def move_out(self):
        while self.stack2:
            self.stack1.append(self.stack2.pop())
    
    def move_in(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())


# Version 3: Version 2的升级版
# 只要stack2中有数字，则每次无论怎么利用stack1倒，stack2在pop时的数字都是一样的 -> 只要stack2不为空，则可不用倒；否则再将stack1中的新内容导入stack2即可
# 具体逻辑：stack2 = reversed(stack1)，因此无论stack1怎么append数字，其新加的数字在stack2中都会被放在stack2[0]，而stack2在pop的时候是取的stack2[-1]
# time: push O(1), pop O(1) ～ O(n)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # 直接判断是否需要将stack1中的新加数据导入stack2
        self.peek()
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack2:
            self.move_in()
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # 这里与前两种方法不同，需要stack1和stack2同时一起判断
        return len(self.stack2) == 0 and len(self.stack1) == 0
    
    def move_in(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
