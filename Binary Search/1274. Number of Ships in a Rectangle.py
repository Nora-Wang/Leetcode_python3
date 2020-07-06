(This problem is an interactive problem.)

On the sea represented by a cartesian plane, each ship is located at an integer point, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true if and only if there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points, which are the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle.  It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example :



Input: 
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
Output: 3
Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
 

Constraints:

On the input ships is only given to initialize the map internally. You must solve this problem "blindfolded". In other words, you must find the answer using the given hasShips API, without knowing the ships position.
0 <= bottomLeft[0] <= topRight[0] <= 1000
0 <= bottomLeft[1] <= topRight[1] <= 1000



#Solution:
'Submissions making more than 400 calls to hasShips will be judged Wrong Answer.' -> binary search to remove the not work range
separate the rectangle to 4 parts + divide and conquer
end case: out of range or hasShips return Fasle -> return 0; hasShips return True and topRight == bottomLeft -> return 1
time: O(n) (wores case is walk through all the positions in the grid), space: O(1)

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        b_x, b_y, t_x, t_y = bottomLeft.x, bottomLeft.y, topRight.x, topRight.y
        if b_x > t_x or b_y > t_y or not sea.hasShips(topRight, bottomLeft):
            return 0
        
        if b_x == t_x and b_y == t_y:
            return 1
        
        mid_x = (t_x + b_x) // 2
        mid_y = (t_y + b_y) // 2
        
        #left_bottom, right_bottom, left_top, right_top
        return self.countShips(sea, Point(mid_x, mid_y), bottomLeft) + \
               self.countShips(sea, Point(t_x, mid_y), Point(mid_x + 1, b_y)) + \
               self.countShips(sea, Point(mid_x, t_y), Point(b_x, mid_y + 1)) + \
               self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1))
        
