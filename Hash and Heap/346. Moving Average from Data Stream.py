Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3


利用deque+sliding window的思想即可完成

#这道题主要是要知道怎么才能返回保留5位小数的方法
1.直接设为0.00000
2.用float()

code:
class MovingAverage(object):

    def __init__(self, size):
        self.queue = collections.deque()
        #self.sum = 0
        self.sum = 0.00000
        self.size = size
        

    def next(self, val):
        self.queue.append(val)
        self.sum += val
        
        if len(self.queue) > self.size:
            temp = self.queue.popleft()
            self.sum -= temp
        
        #return float(self.sum) / len(self.queue)
        return self.sum / len(self.queue)
