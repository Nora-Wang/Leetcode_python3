# 微软面试题，长教训了

import collections
class MinHeap:
    def __init__(self):
        self.data = collections.deque()
        self.count = len(self.data)
    
    # time: O(n)
    def heapify(self, nums):
        if not nums:
            return []

        # 因为在翻转的过程中，就已经把大的数据翻转到了下半部分，因此堆的后半部分一定不用向下换,所以直接从1/2开始,倒序来翻即可
        # 这里用shiftdown之所以是O(n):
        # 是因为从第 N/2 个位置开始往下 siftdown，那么就有大约 N/4 个数在 siftdown 中最多交换 1 次，N/8 个数最多交换 2 次，N/16 个数最多交换 3 次。
        # ???
        for i in range(len(nums) // 2, -1, -1):
            self.shiftdown(nums, i)

    # time: O(logn)
    # append value into heap
    # 整个heap的size是根据push的次数决定的，每次pop的时候并不会改变size
    def heappush(self, value):
        if self.count >= len(self.data):
            self.data.append(value)
        else:
            self.data[self.count] = value
        
        self.count += 1
        self.shiftup(self.data, self.count - 1)
    
    # time: O(logn)
    # pop the min value from min_heap
    def heappop(self):
        if self.count == 0:
            return
        
        temp = self.data[0]
        self.data[0] = self.data[self.count - 1]
        self.count -= 1
        self.shiftdown(self.data, 0)

        return temp

    # time: O(logn)
    # 自底向上翻
    def shiftup(self, nums, index):
        parent_index = (index - 1) // 2
        while index > 0 and nums[index] < nums[parent_index]:
            nums[index], nums[parent_index] = nums[parent_index], nums[index]
            index = parent_index
            parent_index = (index - 1) // 2

    # time: O(logn)
    # 自顶向下翻
    def shiftdown(self, nums, index):
        while index < self.count:
            left_child = index * 2 + 1
            right_child = index * 2 + 2
            min_index = index

            # 找到index，left_child，right_child中最小的那个index
            if left_child < self.count and nums[left_child] < nums[min_index]:
                min_index = left_child
            if right_child < self.count and nums[right_child] < nums[min_index]:
                min_index = right_child
            
            # 当前index已经比左右children都小了，即不用再往下翻了
            if min_index == index:
                break

            nums[index], nums[min_index] =  nums[min_index], nums[index]
            index = min_index
    



