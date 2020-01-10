Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();




思路:使用数组来保存当前集合中的元素，同时用一个hashMap来保存数字与它在数组中下标的对应关系


code:
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.record = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        #若已存在此元素返回false
        if val in self.record:
            return False
        
        #不存在时将新的元素插入数组最后一位，同时更新hashMap
        self.data.append(val)
        self.record[val] = len(self.data) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        #若不存在此元素返回false
        if val not in self.record:
            return False
        
        #存在时先根据hashMap得到要删除数字的下标,以及当前数组的最后一个值
        index = self.record[val]
        last = self.data[-1]
        
        #再将数组的最后一个数放到需要删除的数的位置上,同时更新hashMap中对应的值
        self.data[index] = last
        self.record[last] = index
        
        #删除数组最后一位(用pop),同时更新hashMap
        #list直接pop就是删除最后一个数(参考stack)
        del self.record[val]
        self.data.pop()
        
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        #根据数组的长度来获取一个随机的下标，再根据下标获取元素
        return self.data[random.randint(0, len(self.data) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
