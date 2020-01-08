Implement queue by circulant array. You need to support the following methods:

CircularQueue(n): initialize a circular array with size n to store elements
boolean isFull(): return true if the array is full
boolean isEmpty(): return true if there is no element in the array
void enqueue(element): add an element to the queue
int dequeue(): pop an element from the queue
Example

Example 1:

Input:
CircularQueue(5)
isFull()
isEmpty()
enqueue(1)
enqueue(2)
dequeue()
Output:
["false","true","1"]
Example 2:

Input:
CircularQueue(5)
isFull()
isEmpty()
enqueue(1)
enqueue(2)
dequeue()
dequeue()
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
isFull()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
Output:
["false","true","1","2","true","1","2","3","4","5"]
Notice

it's guaranteed in the test cases we won't call enqueue if it's full and we also won't call dequeue if it's empty. So it's ok to raise exception in scenarios described above.


思路:
我们需要知道队列的入队操作是只在队尾进行的，相对的出队操作是只在队头进行的，所以需要两个变量top与bottom分别来指向队头与队尾;
注意top和bottom的初始值都应该是0,并且都是+1地变化(queue的逻辑理解)

由于是循环队列，我们在增加元素时，如果此时bottom = len(array),bottom需要更新为0;同理,在元素出队时,如果top = len(array),top需要更新为0. 
对此，我们可以直接取模来计算其位置

code:
class CircularQueue:
    def __init__(self, n):
        self.array = [None] * n
        #队头
        self.top = 0
        #队尾
        self.bottom = 0
        #queue的长度
        self.size = 0
    """
    @return:  return true if the array is full
    """
    def isFull(self):
        return self.size != 0 and self.size % len(self.array) == 0

    """
    @return: return true if there is no element in the array
    """
    def isEmpty(self):
        return self.size == 0

    """
    @param element: the element given to be added
    @return: nothing
    """
    def enqueue(self, element):
        #一定要取模,不然会out of index
        self.array[self.bottom % len(self.array)] = element
        self.bottom += 1
        self.size += 1
        
        return

    """
    @return: pop an element from the queue
    """
    def dequeue(self):
        result = self.array[self.top % len(self.array)]
        self.top += 1
        self.size -= 1
        
        return result
