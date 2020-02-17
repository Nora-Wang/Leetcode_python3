Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

 

Example 1:

Input: A = ["tars","rats","arts","star"]
Output: 2
 

Constraints:

1 <= A.length <= 2000
1 <= A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.


Python Union Find过不了

code:
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        self.father = {}
        A = list(set(A))
        
        self.result = len(A)
        
        for word in A:
            self.father[word] = word
        
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i] == A[j]:
                    continue
                if self.check(A[i], A[j]):
                    self.union(A[i], A[j])
            
        return self.result
        
        
    def check(self, a, b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        
        return count == 2
        
    
    def union(self, point_a, point_b):
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        
        if root_a != root_b:
            self.father[root_a] = root_b
            self.result -= 1
            
    def find(self, point):
        path = []
        
        while self.father[point] != point:
            path.append(point)
            point = self.father[point]
        
        for p in path:
            self.father[p] = point
        
        return point
        
