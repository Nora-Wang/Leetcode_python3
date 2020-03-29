There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5

code:
#直解
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        record = [self.helper(i, rating) for i in range(len(rating))]
        
        res = 0
        for i in range(len(rating)):
            small, large = record[i][0], record[i][1]
            
            res += small * large + (i - small) * (len(rating) - (i + 1) - large)
        
        return res
        
    def helper(self, index, rating):
        left = 0
        right = 0
        
        for i in range(index):
            if rating[index] > rating[i]:
                left += 1
        
        for j in range(index + 1, len(rating)):
            if rating[index] < rating[j]:
                right += 1
            
        return (left, right)
 
 
 
 
 
 
 
#DFS
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        self.count = 0
        
        for i in range(len(rating) - 2):
            self.helper1(rating, i+1, [rating[i]])
            self.helper2(rating, i+1, [rating[i]])
        
        return self.count
    
    def helper1(self, rating, index, temp):
        if len(temp) == 3:
            self.count += 1
            return 
        
        for i in range(index, len(rating)):
            if rating[i] <= temp[-1]:
                continue
                
            temp.append(rating[i])
            self.helper1(rating, i+1, temp)
            temp.pop()
            
    def helper2(self, rating, index, temp):
        if len(temp) == 3:
            self.count += 1
            return 
        
        for i in range(index, len(rating)):
            if rating[i] >= temp[-1]:
                continue
                
            temp.append(rating[i])
            self.helper2(rating, i+1, temp)
            temp.pop()
    
                
