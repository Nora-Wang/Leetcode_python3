Given an list interval, which are taking off and landing time of the flight. How many airplanes are there at most at the same time in the sky?

Example

Example 1:

Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
Output: 3
Explanation:
The first airplane takes off at 1 and lands at 10.
The second ariplane takes off at 2 and lands at 3.
The third ariplane takes off at 5 and lands at 8.
The forth ariplane takes off at 4 and lands at 7.
During 5 to 6, there are three airplanes in the sky.
Example 2:

Input: [(1, 2), (2, 3), (3, 4)]
Output: 1
Explanation: Landing happen before taking off.
Notice

If landing and taking off of different planes happen at the same time, we consider landing should happen at first.


code:
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        if not airplanes:
            return 0
            
        line = []
        
        #设置飞行的航线，开始的为+1，降落的为-1
        for airplane in airplanes:
            line.append((airplane.start, 1))
            line.append((airplane.end, -1))
        
        count_planes = 0
        max_planes = 0
        
        #数每个时刻的飞机数目，再更新最大值 
        for _, count in sorted(line):
            count_planes += count
            max_planes = max(max_planes, count_planes)
        
        return max_planes
