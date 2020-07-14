Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

    
#07/14/2020
#time: O(nlogn), space: O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        
        return True
    
    

code:
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        #按start进行排序
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        
        #遍历看看有没有后面区间的头小于前面区间的尾
        for i in range(len(sorted_intervals) - 1):
            if sorted_intervals[i][1] > sorted_intervals[i+1][0]:
                return False
        
        return True
