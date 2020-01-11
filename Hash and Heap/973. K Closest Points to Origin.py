We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000


code:
#brute force
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not points:
            return []
        #注意点1:corner case
        if K >= len(points):
            return points
        
        record = {}
        for node in points:
        #知识点:取根号
            distance = (abs(node[0]) ** 2 + abs(node[1]) ** 2) ** (0.5)
            if distance not in record:
                record[distance] = []
            record[distance].append(node)
        
        #以key=distance为标准对record排序
        #注意这里的结果为list
        sorted_record = sorted(record.items(), key = lambda item:item[0])
        
        result = []
        i = 0
        #这一层的while是用来控制i的值
        #也可以变为for循环
        while len(result) < K:
        #注意点2:sorted_record[i][1]里可能包含多个node,因此不能直接把它加到result中
        #需要每加一个node到result中后,判断一下此时的result是否为K个
            while len(sorted_record[i][1]):
                node = sorted_record[i][1].pop()
                result.append(node)
                if len(result) == K:
                    return result
            i += 1
            
        
