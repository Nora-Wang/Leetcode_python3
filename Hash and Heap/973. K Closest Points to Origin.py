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
            distance = (node[0] ** 2 + node[1] ** 2) ** (0.5)
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
            
            
            
同lintcode 612 https://www.lintcode.com/problem/k-closest-points/description?_from=ladder&&fromId=1

但这个方法无法用于lintcode,因为有个case过不了:当distance相同时,它要求的是按放入原来的顺序输出,但是sorted不能保证这一点
因此lintcode需要使用priority queue来解决问题,即优化版如下:

思路:
#heap == Priority Queue,实现最小堆
heapq在实现过程中就是用的优先队列,即heap的本质为一个queue
其原理是:用heapq.heappush(heap, item)将item放入queue,并且对这个queue按照item的数据从小到大的排序
(这里的item可以是一个元组,eg:(a,b,c),queue通过先比较a,然后比较b,最后比较c的顺序将整个queue按从小到大的排序)
这样在heapq.heappop(heap)时,依照queue的pop原理,应该是pop队头,即整个queue的最小值
这样就满足了最小堆的条件

时间复杂度 O(nlogk)

如果使用 Quick Select 离线算法： 
0. 计算所有的点到原点的 distance -- O(n) 
Quick Select 去找到 kth smallest distance -- O(n) 
遍历所有 distance 找到 top k smallest distance -- O(n) 
找到的 top k smallest points 按 distance 排序并返回 -- O(klogk) 
总共 Quick Select 离线算法耗费时间 O(n + klogk)O(n+klogk) 

#Version priority queue
#leetcode version
import heapq
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not points:
            return []
        
        #定义优先队列
        heap = []
        #遍历所有点并且计算距原点距离，并且距离最远的放优先队列最前面，如果距离一样x较大的放前面 
        #(-dist, -point[0], -point[1])，因为优先队列弹出的是值最小的点，所以需要取负数这样处理 
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, (-distance, -point[0], -point[1]))
            
            #如果队列长度大于所需要的K个值，那就弹出第一个（距离最远）
            if len(heap) > K:
                heapq.heappop(heap)
        
        #把结果放入result中，注意，这里是距离大的在前，所以需要反转结果
        result = []
        for _ in range(K):
            _, x, y = heapq.heappop(heap)
            result.append([-x, -y])
        
        return result[::-1]

       
#lintcode version
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        if not points:
            return []
        
        heap = []
        for node in points:
            distance = self.get_distance(node, origin)
            heapq.heappush(heap, (-distance, -node.x, -node.y))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            result.append([-x,-y])
        
        #result.reverse()
        return result[::-1]
    
    
    def get_distance(self, node, origin):
        return (node.x - origin.x) ** 2 + (node.y - origin.y) ** 2
