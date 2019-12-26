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

思路:
要求调用最少次数的knows() function 来找到名人。我们可以用一个略带greedy的思路，只需要调用 2n 次。第一次先找到可能的名人，第二次再判断该人是否是名人。

首先假设0是名人，ans=0，然后向后遍历，如果发现当前的 result 认识 i，则令 result = i，再继续遍历。最终的result就是名人候选人。
然后再进行第二遍遍历，看result是否有认识的人以及是否有其他人不认识result

knows(A,B)若为True,则抛弃A;否则抛弃B

时间复杂度O(n), 空间复杂度O(1)
code:
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(1, n):
            if knows(result, i):
                result = i
                
        for i in range(n):
            if i != result and (knows(result, i) or not knows(i, result)):
                return -1
            
        return result
