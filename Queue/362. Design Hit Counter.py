Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
Follow up:
What if the number of hits per second could be very large? Does your design scale?


# queue
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.size = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.queue and timestamp - 300 >= self.queue[0]:
            self.pop(timestamp - 300)
        
        self.queue.append(timestamp)
        self.size += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.queue and timestamp - 300 >= self.queue[0]:
            self.pop(timestamp - 300)
        
        return self.size
    
    def pop(self, time):
        while self.queue and self.queue[0] <= time:
            self.queue.popleft()
            self.size -= 1


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)




# Follow up solution:
# 定义了两个大小为300的一维数组time和hits，分别用来保存时间戳和点击数
# 在hit函数中，将时间戳对300取余，然后看此位置中之前保存的时间戳和当前的时间戳是否一样，一样说明是同一个时间戳，那么对应的点击数自增1，如果不一样，说明已经过了五分钟了，那么将对应的点击数重置为1。
# 那么在getHits函数中，我们需要遍历time数组，找出所有在300s内的位置，然后把hits中对应位置的点击数都加起来即可
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = [0] * 300
        self.time = [0] * 300
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        index = timestamp % 300
        
        if timestamp == self.time[index]:
            self.hits[index] += 1
        else:
            self.hits[index] = 1
            self.time[index] = timestamp

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        res = 0
        for i in range(300):
            if timestamp - self.time[i] < 300:
                res += self.hits[i]
        
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
