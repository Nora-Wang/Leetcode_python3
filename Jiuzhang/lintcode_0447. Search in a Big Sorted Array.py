Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).

Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

Example

Example 1:

Input: [1, 3, 6, 9, 21, ...], target = 3
Output: 1
Example 2:

Input: [1, 3, 6, 9, 21, ...], target = 4
Output: -1
Challenge

O(logn) time, n is the first index of the given target number.

Notice

If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2,147,483,647.


code:
"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index, 
        # return 2147483647 if the index is invalid.
"""
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        start = 0
        end = 1
        #由于题目不能直接用len，因此用end*2的方式找到一个比target大的值，即找到一个范围，使其包含target，这样才能在后续用二分法
        while reader.get(end) < target:
            start = end
            end = end * 2
            
        while start + 1 < end:
            mid = start + (end - start) / 2
            #当reader.get(mid) == target时，应该是end=mid，因为可能有比mid更小的值使reader.get(index)=target
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid
        #因为取最小，所以先取start
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
        
