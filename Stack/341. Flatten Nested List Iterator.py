Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
             
             

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        #由于stack的LIFO原则,因此需要将nestedList反一下
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        #题目要求如果hasNext return True, 才会进行next. 
        #即需要通过hasNext函数使得当前stack尾部的NestedInteger满足isInteger
        #因此next函数只需要直接取integer即可
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        #为了让stack的尾部为integer,就需要对尾部的数据类型进行判断
        while self.stack:
            #这里用pop是为了省空间. 
            #因为后续是需要将tail.getList()[::-1]所得到的list里的integers一个一个的放入stack中,若不pop而用下面的写法则会生成新的list
            #self.stack = self.stack[:-1] + tail.getList()[::-1]
            tail = self.stack.pop()
            
            #若为integer,则需要将top重新加入stack中,以便于在next函数中被pop出
            if tail.isInteger():
                self.stack.append(tail)
                return True
            
            self.stack.extend(tail.getList()[::-1])
        
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
