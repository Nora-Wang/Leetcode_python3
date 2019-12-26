Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

 

Example 1:


Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
Example 2:


Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
Output: -1
Explanation: There is no celebrity.
 

Note:

The directed graph is represented as an adjacency matrix, which is an n x n matrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0 means the contrary.
Remember that you won't have direct access to the adjacency matrix.


Intuition:
Consider trust as a graph, all pairs are directed edge.
The point with in-degree - out-degree = N - 1 become the judge.

Explanation:
Count the degree, and check at the end.

code:
Version 1:用list存储
Time Complexity:
Time O(T + N), space O(N)

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        #这里要定义list中存储的值是int,因此一定要加个0
        #注意这里是N+1:这里的意思是一共有N+1个list,count的index最大取值为N;这样才能满足后续i和j的取值(i和j可能取N,因为题目是从1开始取的)
        count = [0] * (N + 1)
        
        for i,j in trust:
            count[j] += 1
            #这里可以用-1,也可以赋值为-1;但要注意不能赋值为0,因为当2，[[1,2],[2,1]]时,count[1] = 1,满足后续条件
            count[i] -= 1
            
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
            
        return -1


Version 2:用hash存储,缺点费空间
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        mapping = {}
        for i in range(N + 1):
            mapping[i] = []
        
        
        for i,j in trust:
            mapping[j].append(i)
            mapping[0].append(i)
            
        for i in range(1, N + 1):
            if len(mapping[i]) == N - 1 and i not in mapping[0]:
                return i
            
        return -1
