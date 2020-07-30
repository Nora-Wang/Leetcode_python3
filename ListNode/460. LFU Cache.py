Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

 

Follow up:
Could you do both operations in O(1) time complexity?

 

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


code:
class Node:
    def __init__(self, key=None, val=None, next=None, prev=None, freq=1):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
        self.freq = freq
        
class DoubleLinkedList:
    def __init__(self):
        self.dummy = Node()
        self.dummy.next = self.dummy.prev = self.dummy
        self.d_size = 0
        
    def __len__(self):
        return self.d_size
    
    def appendleft(self, node):
        node.next = self.dummy.next
        node.prev = self.dummy
        node.next.prev = node
        self.dummy.next = node
        
        self.d_size += 1
    
    def pop(self, node=None):
        if self.d_size == 0:
            return None
        
        if not node:
            node = self.dummy.prev
            
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self.d_size -= 1
        
        return node
    
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        
        # key = freq, value = double linked list with nodes whoes node.freq = freq
        # latest -> oldest
        self.hash_freq = collections.defaultdict(DoubleLinkedList)
        
        # {key:Node}
        self.key_to_nodes = {}
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_nodes:
            return -1
        
        node = self.key_to_nodes[key]
        self.update(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_nodes:
            node = self.key_to_nodes[key]
            self.update(node)
            node.val = value
            return
        
        #print(self.hash_freq[self.min_freq], self.key_to_nodes, self.min_freq)
        
        if self.size == self.capacity:
            node = self.hash_freq[self.min_freq].pop()
            del self.key_to_nodes[node.key]
            self.size -= 1
        
        node = Node(key, value)
        self.key_to_nodes[key] = node
        self.hash_freq[1].appendleft(node)
        self.min_freq = 1
        self.size += 1
        
    def update(self, node):
        freq = node.freq
        
        self.hash_freq[freq].pop(node)
        if self.min_freq == freq and not self.hash_freq[freq].d_size:
            self.min_freq += 1
        
        node.freq += 1
        freq = node.freq
        self.hash_freq[freq].append(node)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
