Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


思路同56,只是需要在开头的时候把newInterval加入intervals,剩下的就是跟56一样


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        result = []
        
        for interval in intervals:
            if len(result) and interval[0] <= result[-1][1]:
                result[-1][1] = max(interval[1], result[-1][1])
            else:
                result.append(interval)
                
        return result



# 分成3段去处理
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0

        # 第一段，把原封不动要放进去的intervals给放进去
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append([intervals[i][0], intervals[i][1]])
            i += 1

        # 第二段，把需要根据newInterval调整的final interval给找出来，然后放进去
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        res.append(newInterval)

        # 第三段，把剩下的intervals放进去
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res
