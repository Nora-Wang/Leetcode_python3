Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


和airplane一样

code:
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        line = []
        for interval in intervals:
            line.append((interval[0], 1))
            line.append((interval[1], -1))
        
        max_count = 0
        curt_count = 0
        
        for _,count in sorted(line):
            curt_count += count
            max_count = max(max_count, curt_count)
        
        return max_count
