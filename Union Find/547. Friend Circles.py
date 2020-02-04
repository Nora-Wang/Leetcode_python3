There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:

N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.


code:
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not len(M) or not len(M[0]):
            return 0
        
        self.father = {}
        
        #难点:分析清楚怎么存储数据
        for i in range(len(M)):
            self.father[i] = i
        
        #先设置为len(M),后面发现两个相等时,直接-1即可
        self.count = len(M)
        
        for i in range(len(M)):
            for j in range(i + 1):
                if M[i][j] == 1:
                    self.union(M, i, j)
        
        return self.count
    
    def union(self, M, point_a, point_b):
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count -= 1
        
    def find(self, point):
        path = []
        
        while self.father[point] != point:
            path.append(point)
            point = self.father[point]
        
        for p in path:
            self.father[p] = point
        
        return point
        
        
