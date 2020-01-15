Implement a data structure, provide two interfaces:

add(number). Add a new number in the data structure.
topk(). Return the top k largest numbers in this data structure. k is given when we create the data structure.
Example

Example1

Input: 
s = new Solution(3);
s.add(3)
s.add(10)
s.topk()
s.add(1000)
s.add(-99)
s.topk()
s.add(4)
s.topk()
s.add(100)
s.topk()
		
Output: 
[10, 3]
[1000, 10, 3]
[1000, 10, 4]
[1000, 100, 10]

Explanation:
s = new Solution(3);
>> create a new data structure, and k = 3.
s.add(3)
s.add(10)
s.topk()
>> return [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> return [1000, 10, 3]
s.add(4)
s.topk()
>> return [1000, 10, 4]
s.add(100)
s.topk()
>> return [1000, 100, 10]
Example2

Input: 
s = new Solution(1);
s.add(3)
s.add(10)
s.topk()
s.topk()

Output: 
[10]
[10]

Explanation:
s = new Solution(1);
>> create a new data structure, and k = 1.
s.add(3)
s.add(10)
s.topk()
>> return [10]
s.topk()
>> return [10]


直接用heap即可,注意这里的return topk不是要将其pop出,因此直接将sorted的结果return即可,因此sorted函数的结果为list

code:
import heapq
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.k = k
        self.heap = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        heapq.heappush(self.heap, num)
        

    """
    @return: Top k element
    """
    def topk(self):
        #heap长度大于k时,将多的较小的数pop出
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return sorted(self.heap, reverse = True)
