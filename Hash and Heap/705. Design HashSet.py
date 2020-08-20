Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.


# use open hashing way to solve this probelm
# same as 706. Design HashMap
# add: time: O(n), n = length of longest linkedlist in one index
# remove: time: O(n), n = length of longest linkedlist in one index
# contains: time: O(n), n = length of longest linkedlist in one index

# time: O(n), n = length of longest linkedlist in one index
# space: O(1000000), capacity from the question
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 1000
        self.list = [None] * self.capacity
        self.size = 0

    def add(self, key: int) -> None:
        self.size += 1
        valid_key = key % self.capacity
        
        # this valid_key index haven't been used 
        if not self.list[valid_key]:
            self.list[valid_key] = ListNode(key)
            return
        
        # check whether key has already existed in this linkedlist
        head = self.list[valid_key]
        while head.next:
            if head.val == key:
                # means key has already existed -> don't need to add size
                self.size -= 1
                break
                
            head = head.next
        
        # not exist -> append to the end of the linkedlist
        if head.val != key:
            head.next = ListNode(key)
        
        return

    def remove(self, key: int) -> None:
        if self.size == 0:
            return
        
        valid_key = key % self.capacity
        
        # whether key exist in the hashset, the prev node of the key, curt linkedlist node for key, the dummy node for the linkedlist
        exist, prev, curt, dummy = self.exist_location(key)
        
        # not exist in the linkedlist or the index
        if not exist:
            return
        
        # remove node
        prev.next = curt.next
        self.list[valid_key] = dummy.next
        
        self.size -= 1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if self.size == 0:
            return False
        
        exist, _, _, _ = self.exist_location(key)
        
        return exist
    
    def exist_location(self, key: int):
        valid_key = key % self.capacity
        
        # this index haven't been used -> not exist
        if not self.list[valid_key]:
            return False, None, None, None
        
        exist = False
        
        # find the key in the linkedlist
        dummy = prev = ListNode()
        dummy.next = curt = self.list[valid_key]
        while curt:
            if curt.val == key:
                exist = True
                break
            prev = curt
            curt = curt.next
        
        return exist, prev, curt, dummy


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
