Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.



key和value被当作一组pair放在hash表中,当key值被映射到hash表的同一位置时,会发生conflict,这时为解决冲突会有两种方法open hashing和close hashing.
一般来说open hashing更简单,而且更好用.因此,这道题目其实就是写一个open hashing.

open hashing其实就是当发生conflict时,将统一index的pairs以链表的方式进行存储;
即不同key值通过hash function后得到的相同hash[index]以linkedlist的方式存储很多pairs(keys, values)


code:
class ListNode(object):
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None
        
class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #1000这个值是由题目Note里的信息计算得出;后续的取模即实现hash function的功能
        self.size = 1000
        self.array = [None] * self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        #hash function
        index = key % self.size
        
        #若为空,则直接加入pair;否则,在该hash[index]的linkedlist中找有没有同样key值的pair,若有,更新value值;若没有则新加入一组pair
        if self.array[index] == None:
            self.array[index] = ListNode(key, value)
        else:
            curt = self.array[index]
            while True:
                if curt.pair[0] == key:
                    curt.pair = (key, value)
                    return
                if curt.next == None:
                    curt.next = ListNode(key, value)
                    return
                curt = curt.next
            
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.size
        
        #存在的情况只有当hash[index]的linkedlist中出现了key值才能有value;否则不管是hash[index]为空还是linkedlist中不存在该key值,其结果都是-1
        curt = self.array[index]
        while curt:
            if curt.pair[0] == key:
                return curt.pair[1]
            curt = curt.next

        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key % self.size
        #不存在key
        if self.array[index] == None:
            return
        
        #一定要单独判断一下curt,因为后续当需要删除一个链表的curt point时,一定是prev.next = curt.next,而prev则需要被提供
        #这一步排除了curt是key的情况,即即便是出现key,也只能是curt.next这个点,此时prev最早也是curt
        curt = self.array[index]
        if curt.pair[0] == key:
            self.array[index] = curt.next
            
        prev = curt
        curt = curt.next
        while curt:
            if curt.pair[0] == key:
                prev.next = curt.next
                return
            prev, curt = prev.next, curt.next
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
