Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false


这道题的解法有3种情况


1.要求add和find的时间复杂度较平均
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.dic = []
        
    #insert sort:先将number放入数组的最后一位，然后依次与前一个数做大小比较，若小，则swap
    def add(self, number):
        self.dic.append(number)
        index = len(self.dic) - 1
        
        #while循环记得写index -= 1！！！！
        while index > 0:
            if self.dic[index] < self.dic[index - 1]:
                self.dic[index - 1], self.dic[index] = self.dic[index], self.dic[index - 1]
            index -= 1
                

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    #two pointer模板,value相当于target
    def find(self, value):
        
        start, end = 0, len(self.dic) - 1
        
        while start < end:
            if self.dic[start] + self.dic[end] == value:
                return True
            if self.dic[start] + self.dic[end] < value:
                start += 1
            else:
                end -= 1
                
        return False
      
2.add调用的很多，而find调用的很少；即要求add的时间复杂度到最低
这种解法:find为O(n),add为O(1)
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.dic = {}
        
    def add(self, number):
        if number in self.dic:
            self.dic[number] += 1
        else:
            self.dic[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        for num in self.dic:
            if value - num in self.dic and (value - num != num or self.dic[num] > 1):
                return True
                
        return False

3.find调用的很多，而add调用的很少；即要求find的时间复杂度到最低
这种解法:add为O(n),find为O(1)
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.dic = []
        self.sum = set()
        
    def add(self, number):
        for num in self.dic:
            self.sum.add(num + number)
        self.dic.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        return value in self.sum
