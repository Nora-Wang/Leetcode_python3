Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


code:
LinkedList Version
class ListNode(object):
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        #用于记录该key对应的prev的值
        self.key_to_prev = {}
        #用于记录key出现的时间,头是最早出现的,尾是最新出现过的key
        self.dummy = ListNode()
        #用于记录链表的尾
        self.tail = self.dummy
    
    #当key被使用后,更新一下链表的内容
    def update_dummy(self, key):
        prev = self.key_to_prev[key]
        curt = prev.next

！！！！#这个特判很容易忘记！
        if curt == self.tail:
            return
        
        #delete curt
        prev.next = curt.next
        
        #update hash
        self.key_to_prev[curt.next.key] = prev
        
        self.push(curt)
    
    #在出现新的point的时候,将该点的key放入链表的尾部,同时更新hash表
    def push(self, curt):
        self.key_to_prev[curt.key] = self.tail
        curt.next = None
        self.tail.next = curt
        self.tail = curt
    
    #得到数据,并更新链表
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_prev:
            return -1
        
        self.update_dummy(key)
        
        return self.key_to_prev[key].next.value
       
    #当hash表长度超过capacity时,需要将最早出现的head给删掉,同时更新head.next的hash表(因为里面存储的是其对应的prev)
    def pop_front(self):
        head = self.dummy.next
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
        del self.key_to_prev[head.key]
    
    #要分情况,若key在hash表中,直接更新一下value,然后更新一下链表即可;若不在,则需要新建一个point,然后将其放入hash中,注意hash长度,以 判断是否需要pop
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_to_prev:
            self.key_to_prev[key].next.value = value
            self.update_dummy(key)
            return
        
        new_node = ListNode(key, value)
        #1.可直接用push function
        self.push(new_node)
        #2.单独写,但是有的重复,而且容易写错:先将新点放在tail后,然后renew dummy,最后renew tail
        self.tail.next = new_point
        self.key_to_prev[key] = self.tail
        self.tail = new_point
        
        if len(self.key_to_prev) > self.capacity:
            self.pop_front()
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


***************************************************************************
Hash Version
#主要是将self.keys作为一个key出现先后的记录,每次用了key就先remove,然后重新append
#这样就可以保证self.keys中的最后一位是最新用过的,而第一位是最老的
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.record = {}
        self.keys = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.record:
            self.keys.remove(key)
            self.keys.append(key)
            return self.record[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #这里直接将value赋值即可,因为无论需不需要初始化,都可以这样写
        #这里的意思是,若self.record存在key,则将其重新赋值为value;若self.record不存在key,则新建一个item
        self.record[key] = value
        
        #因为前一句话,key一定会在self.record中,但是由于不知道key是否已经存在于self.keys中,需要提前判断一下,如果在则需要提前删除,然后才能加入
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        
        if len(self.record) > self.capacity:
            del self.record[self.keys[0]]
            self.keys = self.keys[1:]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
